import base64
import requests
import json

url = 'https://www.virustotal.com/api/v3/files/{}'.format('927fa50bd00ca0775faee9c912d8ba96952280093671745ba5c61969234bfe87')

header = {'x-apikey': '97effa9293fe867afcff9a79a75b2bfe547cafa222b7bc7bc0cc6bf13d713429'}

rq = requests.get(url, headers = header, verify=False)
print (rq.json())