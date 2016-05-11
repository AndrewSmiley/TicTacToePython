__author__ = 'Andrew'
import requests
url = "https://api.newrelic.com/v2/servers.json"
headers = {'X-Api-Key':'5708afa9e062b1806d6c871c04593e5bb2eb6347539b5ce'}
params = {'names[]':'System/Memory/Used/bytes'}
r = requests.get(url, params=params, headers=headers)
print  r.text