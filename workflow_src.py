from urllib import request
import json

query = "{query}"

answer = {"items": [
]}

resp = request.urlopen(f"https://api.urbandictionary.com/v0/define?term={query}")

text = resp.read()
json_resp = json.loads(text)

for item in sorted(json_resp['list'], key=lambda d: d['thumbs_up'], reverse=True):
    answer['items'].append(
        {
            "uid": item['thumbs_up'],
            "type": "default",
            "title": item['definition'],
            "subtitle": f"\U0001F44D: {item['thumbs_up']}, \U0001F44E: {item['thumbs_down']}",
            "arg": item['permalink'],
            "icon": {
                "path": "./ub.ico"
            },
            "quicklookurl": item['permalink'],
        }
    )

print(json.dumps(answer))
