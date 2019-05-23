# import requests library
import requests

#import json library
import json

controller='sandboxapic.cisco.com

url = "https://" + controller + "/api/v1/ticket"
payload = {"username":"devnetuser","password":"Cisco123!"}


header = {"content-type": "application/json"}
response= requests.post(url,data=json.dumps(payload), headers=header, verify=Fals
r_json=response.json()

print(r_json)
ticket = r_json["response"]["serviceTicket"]
url = "https://" + controller + "/api/v1/host?limit=1&offset=1"
header = {"content-type": "application/json", "X-Auth-Token":ticket}
response = requests.get(url, headers=header, verify=False)

print ("Hosts = ")
print (json.dumps(response.json(), indent=4, separators=(',', ': ')))

r_resp=response.json()

print(r_resp["response"][0]["hostIp"])

