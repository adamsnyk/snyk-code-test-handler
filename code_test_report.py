import json
import pprint
import sys

code_json=json.load(sys.stdin)

results = code_json['runs'][0]['results']

simple_results = []
for result in results:
    simple_result = {}
    simple_result['type'] = result['ruleId']
    simple_result['level'] = result['level']
    simple_result['message'] = result['message']['text']
    simple_result['file'] = result['locations'][0]['physicalLocation']['artifactLocation']['uri']
    simple_result['lines'] = '{} - {}'.format(
        result['locations'][0]['physicalLocation']['region']['startLine'],
        result['locations'][0]['physicalLocation']['region']['endLine']
    )
    simple_results.append(simple_result)


pprint.pprint(simple_results)
print("\nTotal Issues: {}\n".format(len(simple_results)))