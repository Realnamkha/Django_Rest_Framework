import requests

# endpoint = "https://httpbin.org/#/Status_codes"
# endpoint =  "https://httpbin.org/status/200/"
endpoint = "http://127.0.0.1:8000/api/"
get_response = requests.get(endpoint)

# Check if the request was successful (status code 200)
print(get_response.json())
