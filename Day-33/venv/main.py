import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
# response.raise_for_status() will raise an HTTPError if the HTTP request return an un-successful status code.
response.raise_for_status()
print(response)

data = response.json()
print(data)

# to print a specific location from response
data = response.json()["iss_position"]
print(data)

latitude = response.json()["iss_position"]["latitude"]
print(latitude)
longitude = response.json()["iss_position"]["longitude"]
print(longitude)