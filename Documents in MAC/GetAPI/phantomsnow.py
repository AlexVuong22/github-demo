import requests
import json

AUTH_TOKEN = "4krLQtfWPD7AAZGvQPvSKUNL6b1fclZnNQwuDmqwDso="
PHANTOM_SERVER = "192.168.1.10"
LABEL = "warning"

url = 'https://{}/rest/container'.format(PHANTOM_SERVER)

container_common = {
    "description": "Test container added via REST API call",
}

data_request = container_common
data_request['name'] = '{} ({})'.format("tuyet", "7722")
data_request = json.dumps(data_request)

headers_request = {
  "ph-auth-token": AUTH_TOKEN
}

r = requests.post(url, data = data_request, headers = headers_request, verify=False)