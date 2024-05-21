import requests
import json
url = "http://192.168.1.19:8000/services/search/jobs/1671527242.141/acl"
url1= "https://192.168.1.19:8089/services/search/jobs/1671527242.141/acl"
data = {"perms.read":"*",
        "sharing": "global"}
json_data = json.dumps(data)
r = requests.post(url1,data=json_data,verify=False)
print (r)