import requests

URL = "https://google.com"

try:
    response = requests.head(URL, allow_redirects=True)
except Exception as e:
    print(f"NOT OK: {str(e)}")
else:
    if response.status_code == (200):
        print("OK")
    else:
        print(f"NOT OK: HTTP response code {response.status_code}")
