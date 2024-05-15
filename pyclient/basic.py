import requests

# endpoint = "https://httpbin.org/#/Status_codes"
# endpoint =  "https://httpbin.org/status/200/"
endpoint = "http://127.0.0.1:8000/api/"
get_response = get_response = requests.post(endpoint, json={"title": "Abc123"})
print(get_response.json())
