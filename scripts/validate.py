#!/usr/bin/env python3
"""Static validation only; does not execute n8n or verify business logic."""
import json, pathlib, re
root=pathlib.Path(__file__).resolve().parents[1]
paths=sorted((root/'workflows').glob('*.json'))
assert len(paths)==6, f'Expected six JSON files, got {len(paths)}'
for p in paths:
    data=json.loads(p.read_text())
    names={node['name'] for node in data['nodes']}
    assert names
    for origin,conns in data.get('connections',{}).items():
        assert origin in names,(p,origin)
        for branch in conns.get('main',[]):
            for edge in branch:
                assert edge['node'] in names,(p,edge)
    s=p.read_text()
    forbidden=['appz9AMiW3KbFFhRZ','nexkeycollective.com','deals@nexkeycollective.com','917-608-8224','49da069b-cf46-414f-ad7a-f2e782f83e05']
    assert not any(v in s for v in forbidden),p
    assert not re.search(r'Bearer\s+[A-Za-z0-9_-]{16,}',s),p
    assert '"credentials"' not in s,p
    assert data.get('active') is False,p
    print(f'OK: {p.name}: {len(data["nodes"])} nodes')
print('PASS: six JSON workflows structurally valid; no known original secrets/identifiers detected.')
print('NOTE: This is NOT a comprehensive secret audit or a live execution test.')
