#!/usr/bin/env python3
"""Offline package integrity checks, not hosted behavior qualification."""
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILLS = {
    'tpm-runtime-onboarding', 'tpm-onboarding-planning', 'tpm-status-attention',
    'tpm-daily-snapshot', 'tpm-reporting', 'tpm-stakeholder-followup', 'tpm-closeout',
}
EXCLUDED = {'.git', 'dist', '__pycache__', 'private', 'local'}


def source_files(root=ROOT):
    return sorted(p for p in root.rglob('*') if p.is_file()
                  and not any(part in EXCLUDED for part in p.relative_to(root).parts)
                  and p.suffix != '.pyc')


def validate(root=ROOT):
    errors = []
    required = ['README.md', 'VERSION', 'LICENSE', 'agent/instructions.md',
                'agent/operating-contract.md', 'agent/acceptance-tests.md',
                'deployment/deployment.example.json', 'prompts/create-workspace-agent.md']
    for rel in required:
        if not (root / rel).is_file():
            errors.append(f'Missing required file: {rel}')
    actual = {p.name for p in (root / 'skills').iterdir() if p.is_dir()}
    if actual != SKILLS:
        errors.append(f'Skill set mismatch: {actual ^ SKILLS}')
    for name in sorted(SKILLS):
        path = root / 'skills' / name / 'SKILL.md'
        if not path.is_file():
            errors.append(f'Missing skill: {name}')
            continue
        text = path.read_text()
        frontmatter = re.match(r'^---\n(.*?)\n---\n', text, re.S)
        if not frontmatter or f'name: {name}\n' not in frontmatter.group(1) + '\n':
            errors.append(f'Invalid skill name/frontmatter: {name}')
        if not frontmatter or not re.search(r'^description: .+', frontmatter.group(1), re.M):
            errors.append(f'Missing skill description: {name}')
    files = source_files(root)
    for path in files:
        rel = path.relative_to(root)
        if path.is_symlink():
            errors.append(f'Symlink is not portable: {rel}')
            continue
        try:
            text = path.read_text(encoding='utf-8')
        except UnicodeError:
            errors.append(f'Unexpected binary in source package: {rel}')
            continue
        if path.suffix == '.json':
            try:
                json.loads(text)
            except ValueError as exc:
                errors.append(f'Invalid JSON: {rel}: {exc}')
        # Detect common accidental credentials and local user paths without printing content.
        patterns = [r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
                    r'gh[pousr]_[A-Za-z0-9]{20,}', r'sk-[A-Za-z0-9]{30,}',
                    r'/Users/[A-Za-z0-9._-]+/', r'C:\\Users\\[^\\\s]+\\']
        if any(re.search(p, text) for p in patterns):
            errors.append(f'Potential private material: {rel}')
        if path.suffix == '.md' or path.name.endswith('.md.txt'):
            for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
                target = target.strip('<>')
                if urlsplit(target).scheme or target.startswith('#'):
                    continue
                local = unquote(target.split('#', 1)[0])
                if local and not (path.parent / local).exists():
                    errors.append(f'Broken local link: {rel} -> {local}')
    # Validate a connected one-project bundle, not just standalone JSON syntax.
    fixture = root / 'examples' / 'example-launch'
    registry = json.loads((fixture / 'registry/projects.json').read_text())
    entries = registry['projects']
    if len(entries) != 1 or entries[0]['project_id'] != 'example-launch':
        errors.append('Example registry must resolve exactly one expected project')
    else:
        config_path = (fixture / 'registry' / entries[0]['current_config']).resolve()
        config = json.loads(config_path.read_text())
        if config['project_id'] != entries[0]['project_id']:
            errors.append('Registry and config project mismatch')
        for key, pointer in config['current'].items():
            dest = config_path.parent / pointer
            if not dest.is_file():
                errors.append(f'Unresolved example current pointer: {key}')
            elif dest.suffix == '.json' and json.loads(dest.read_text()).get('project_id') != config['project_id']:
                errors.append(f'Cross-project example pointer: {key}')
        source_map = json.loads((config_path.parent / config['current']['source_map']).read_text())
        for pointer in source_map['category_roots'].values():
            if not (config_path.parent / pointer).is_file():
                errors.append(f'Unresolved category root: {pointer}')
        evidence = json.loads((config_path.parent / 'evidence.json').read_text())['evidence']
        ids = [item['evidence_id'] for item in evidence]
        if len(ids) != len(set(ids)) or any(item['project_id'] != config['project_id'] for item in evidence):
            errors.append('Duplicate evidence IDs or cross-project evidence')
        for item in evidence:
            if not all(item.get(k) for k in ['source_id', 'source_url', 'event_at', 'retrieved_at', 'classification']):
                errors.append('Incomplete evidence provenance')
    deployment = json.loads((root / 'deployment/deployment.example.json').read_text())
    if deployment['sharepoint']['hostname'] is not None or deployment['schedules']:
        errors.append('Public deployment example must have no live storage host or schedules')
    if errors:
        for error in errors:
            print('FAIL:', error, file=sys.stderr)
        return False
    print(f'PASS: {len(files)} source files; seven skills; JSON, links, provenance and fixture pointers checked.')
    print('Scope: offline structural validation only. Hosted behavior and live integrations unverified.')
    return True


if __name__ == '__main__':
    raise SystemExit(0 if validate() else 1)
