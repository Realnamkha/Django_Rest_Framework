import requests

# endpoint = "https://httpbin.org/#/Status_codes"
# endpoint =  "https://httpbin.org/status/200/"
headers = {'Authorization': 'Bearer f0fcd60d9d4b7185363d3eaa61e645d86c22bdde'}
endpoint = "http://127.0.0.1:8000/api/products/"
data = {
    "title" : "MACBOOK M22",
    "price" : 1500
 }
get_response = requests.post(endpoint,json=data,headers=headers)
print(get_response.json())