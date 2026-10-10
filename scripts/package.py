#!/usr/bin/env python3
"""Build deterministic, dependency-free source and skill archives."""
import hashlib
import json
import re
import zipfile
from pathlib import Path
from validate import ROOT, SKILLS, source_files, validate


def archive(path, contents):
    with zipfile.ZipFile(path, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as output:
        for name, content in sorted(contents.items()):
            item = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            item.compress_type = zipfile.ZIP_DEFLATED
            item.external_attr = 0o100644 << 16
            output.writestr(item, content, compresslevel=9)


def main():
    if not validate():
        raise SystemExit(1)
    version = (ROOT / 'VERSION').read_text().strip()
    if not re.fullmatch(r'\d+\.\d+\.\d+', version):
        raise SystemExit('VERSION must be numeric major.minor.patch')
    dist = ROOT / 'dist'
    (dist / 'skill-packages').mkdir(parents=True, exist_ok=True)
    source = {str(p.relative_to(ROOT)): p.read_bytes() for p in source_files()}
    manifest = {'version': version, 'files': {p: hashlib.sha256(b).hexdigest() for p, b in sorted(source.items())}}
    manifest_bytes = (json.dumps(manifest, indent=2) + '\n').encode()
    (dist / 'manifest.json').write_bytes(manifest_bytes)
    package = dict(source)
    package['manifest.json'] = manifest_bytes
    for name in sorted(SKILLS):
        prefix = f'skills/{name}/'
        contents = {p[len(prefix):]: b for p, b in source.items() if p.startswith(prefix)}
        path = dist / 'skill-packages' / f'{name}.zip'
        archive(path, contents)
        package[f'skill-packages/{name}.zip'] = path.read_bytes()
    release = dist / f'agentic-tpm-workspace-starter-{version}.zip'
    archive(release, package)
    digest = hashlib.sha256(release.read_bytes()).hexdigest()
    (dist / f'{release.name}.sha256').write_text(f'{digest}  {release.name}\n')
    print(f'Built {release.name} and seven skill archives. SHA-256: {digest}')


if __name__ == '__main__':
    main()
