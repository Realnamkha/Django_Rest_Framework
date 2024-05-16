import requests

# endpoint = "https://httpbin.org/#/Status_codes"
# endpoint =  "https://httpbin.org/status/200/"
endpoint = "http://127.0.0.1:8000/api/products/"
data = {
    "title" : "MACBOOK M2",
    "price" : 1500
 }
get_response = requests.post(endpoint,json=data)
print(get_response.json())