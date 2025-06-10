#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from json import load, dumps

with open('_site/v1/index.json', 'r', encoding='utf-8') as f:
    data = load(f)

with open('metabolism/run/output/index.json', 'r', encoding='utf-8') as f:
    has_updated_sha = load(f)

mc_pkg = [pkg for pkg in data['packages'] if pkg['uid'] == 'net.minecraft'][0]
mc_pkg['sha256'] = has_updated_sha['packages'][0]['sha256']

with open('_site/v1/index.json', 'w', encoding='utf-8') as f:
    f.write(dumps(data, indent=2, ensure_ascii=False) + '\n')

print(f"Updated net.minecraft sha256 to {mc_pkg['sha256']} in _site/v1/index.json")
