import requests
import urllib.parse
import os

from bs4 import BeautifulSoup

os.environ['http_proxy'] = HTTP_PROXY
# os.environ['HTTP_PROXY'] = HTTP_PROXY
os.environ['https_proxy'] = HTTPS_PROXY
# os.environ['HTTPS_PROXY'] = HTTPS_PROXY
os.environ['NO_PROXY'] = NO_PROXY
# Define the Webex Teams authorization endpoint URL and the Redirect URI
authorization_endpoint = "https://api.ciscospark.com/v1/authorize"
redirect_uri = "https://myapp.com/callback"

# Define the parameters for the authorization endpoint URL
params = {
    "client_id": "",
    "redirect_uri": redirect_uri,
    "response_type": "code",
    "scope": "spark:messages_write"
}

# Redirect the user to the authorization endpoint URL
url = f"{authorization_endpoint}?{urllib.parse.urlencode(params)}"
requests.get(url)

# Use the temporary authorization code to request an access token from the Webex Teams token endpoint
token_endpoint = "https://api.ciscospark.com/v1/access_token"

data = {
    "grant_type": "authorization_code",
    "code": "",
    "redirect_uri": redirect_uri,
    "client_secret":"",
    "client_id": ""
}

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

response = requests.post(token_endpoint, data=data, headers=headers)

if response.status_code == 200:
    access_token = response.json()["access_token"]
    # Store the access token securely in your code
    print(access_token)

    # Use the access token to make API requests
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get("https://api.ciscospark.com/v1/rooms", headers=headers)
    # Handle the API response as needed
else:
  print(response.text)
