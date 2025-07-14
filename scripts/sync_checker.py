#!/usr/bin/env python3
import json, hashlib
from pathlib import Path

with open('digest_map.json') as f:
    digests = json.load(f)

for path, sha in digests.items():
    if not Path(path).exists():
        print(f"Missing {path}")
        continue
    current = hashlib.sha256(Path(path).read_bytes()).hexdigest()
    if current != sha:
        print(f"Drift detected in {path}")
