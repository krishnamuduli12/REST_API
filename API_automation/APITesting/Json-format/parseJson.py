import json

odics = '{"k1":"Val1","k2":"val2" }'

json_result = json.loads(odics)
print(json_result['k1'])