import sys
import requests
import json

if len(sys.argv) != 2:
    sys.exit("Bye!")

urls = "https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1]
response = requests.get(url=urls)
# print(json.dumps(response.json(), indent=2))

o = response.json()
for result in o["results"]:
    print(result["trackName"])
