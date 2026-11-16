#!/usr/bin/env python3
"""Launch SpeedBreaker Carbon and back up its private portable saves."""
from pathlib import Path
from datetime import datetime
import subprocess, sys, zipfile

root = Path(__file__).resolve().parents[1]
runtime = root / 'SpeedBreaker-Carbon'
if not (runtime / 'speedbreaker.sh').is_file() or not (runtime / 'data/game/default.xex').is_file():
    raise SystemExit('Install the official runtime and your own Collector\'s Edition game data first.')
for folder in ('logs', 'backups'):
    (root / folder).mkdir(exist_ok=True)

def backup():
    userdata = runtime / 'data/save'
    files = [p for p in userdata.rglob('*') if p.is_file() and 'cache' not in p.relative_to(userdata).parts and p.suffix not in ('.log', '.dmp')]
    if not files:
        return
    dest = root / 'backups' / ('userdata-' + datetime.now().strftime('%Y%m%d-%H%M%S-%f') + '.zip')
    with zipfile.ZipFile(dest, 'w', zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, path.relative_to(userdata))

backup()
with (root / 'logs/session.log').open('a') as log:
    log.write('\nSession ' + datetime.now().isoformat() + '\n'); log.flush()
    result = subprocess.run([str(runtime / 'speedbreaker.sh'), *sys.argv[1:]],
                            cwd=runtime, stdout=log, stderr=subprocess.STDOUT)
backup()
raise SystemExit(result.returncode)
