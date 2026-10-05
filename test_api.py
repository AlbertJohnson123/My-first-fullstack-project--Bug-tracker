import requests
import json

reqUrl = "http://127.0.0.1:5000/api/tickets"

headersList = {
 "Accept": "*/*",
 "User-Agent": "Thunder Client (https://www.thunderclient.com)",
 "Content-Type": "application/json" 
}

payload = json.dumps({
  "title":"button not working",
  "description":"not working",
  "priority":"high"
})

response = requests.request("POST", reqUrl, data=payload,  headers=headersList)

print(response.text)