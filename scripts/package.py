#!/usr/bin/env python3
"""Create one single-root ZIP per skill for manual import. No upload occurs."""
from pathlib import Path
import zipfile
import stat

def linked(path):
    info = path.lstat()
    return stat.S_ISLNK(info.st_mode) or bool(getattr(info, "st_file_attributes", 0) & 0x400)

ROOT = Path(__file__).resolve().parents[1]

def main():
    out = ROOT/'dist'
    out.mkdir(exist_ok=True)
    count = 0
    for skill in sorted((ROOT/'skills').iterdir()):
        if linked(skill):
            raise ValueError('Refusing to package link/junction ' + str(skill))
        if not skill.is_dir():
            continue
        archive = out/(skill.name + '.zip')
        with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as bundle:
            for file in sorted(skill.rglob('*')):
                if linked(file):
                    raise ValueError('Refusing to package link/junction ' + str(file))
                if file.is_file() and '__pycache__' not in file.parts and file.suffix != '.pyc':
                    bundle.write(file, (Path(skill.name)/file.relative_to(skill)).as_posix())
        with zipfile.ZipFile(archive) as bundle:
            names = bundle.namelist()
            assert names.count(skill.name + '/SKILL.md') == 1
            assert all(name.startswith(skill.name + '/') and '..' not in Path(name).parts for name in names)
        count += 1
    print('Created', count, 'single-skill ZIPs in dist/')
if __name__ == '__main__':
    main()
