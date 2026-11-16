#!/usr/bin/env python3
"""Install verified SpeedBreaker Carbon on Linux using your own Collector's Edition dump."""
from pathlib import Path
import argparse, hashlib, shutil, subprocess, tarfile

EXPECTED = '0ad165dafc0af5f8891ebd89e70c17a1b56ed70f412e6ac978af49e764bcc600'

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--game', required=True, type=Path, help='Your disc ISO or extracted folder')
    parser.add_argument('--runtime-archive', required=True, type=Path)
    parser.add_argument('--destination', type=Path, default=Path.home() / 'Games/NFSCarbonCE')
    args = parser.parse_args()
    dest = args.destination.expanduser().resolve()
    if not args.game.exists():
        parser.error('Game source not found.')
    if dest.exists():
        parser.error('Destination exists; choose a new directory to preserve saves and settings.')
    with args.runtime_archive.open('rb') as f:
        if hashlib.file_digest(f, 'sha256').hexdigest() != EXPECTED:
            parser.error('Runtime hash differs from upstream v0.1.3.')
    with tarfile.open(args.runtime_archive) as archive:
        for entry in archive.getmembers():
            path = Path(entry.name)
            if path.is_absolute() or '..' in path.parts or path.parts[0] != 'SpeedBreaker-Carbon':
                parser.error('Unsafe archive member.')
        dest.mkdir(parents=True)
        archive.extractall(dest, filter='data')
    runtime = dest / 'SpeedBreaker-Carbon'
    (runtime / 'portable.txt').touch()
    subprocess.run([str(runtime / 'speedbreaker.sh'), '--install', str(args.game.resolve())], cwd=runtime, check=True)
    subprocess.run([str(runtime / 'speedbreaker.sh'), '--verify', str(runtime / 'data/game')], cwd=runtime, check=True)
    source = Path(__file__).resolve().parents[1]
    shutil.copy2(source / 'settings.toml', runtime / 'data/settings.toml')
    shutil.copytree(source / 'source', dest / 'source', ignore=shutil.ignore_patterns('__pycache__'))
    shutil.copy2(source / 'jogar.sh', dest / 'jogar.sh')
    (dest / 'jogar.sh').chmod(0o755)
    print('Installed:', dest)
    print('Add jogar.sh to Steam as a non-Steam game. Leave forced compatibility disabled.')

if __name__ == '__main__':
    main()
