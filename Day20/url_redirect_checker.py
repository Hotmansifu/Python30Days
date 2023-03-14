import requests

url = input("Enter URL to check: ")

response = requests.get(url, allow_redirects=True)

print("Initial URL:", url)
print("Final URL:", response.url)
print("Status Code:", response.status_code)

headers = response.headers
print("Headers:")
for header in headers:
    print(header+":", headers[header])
