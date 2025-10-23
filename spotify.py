import requests
import base64
import json
from creds import client_id, client_secret

def get_token():
  '''Function to grab my spotify token'''

  # The URL where we send our POST request to get the token
  url = "https://accounts.spotify.com/api/token"

  # Combine the client ID and client secret into one string
  # This identifies our app (like a username:password combo)
  cred_string = f"{client_id}:{client_secret}"

  # Base64 makes it web-safe to send through the internet
  # Because it might include special characters like @ :
  byte_creds = cred_string.encode('utf-8')

  # Convert the cred_string into Bytes (computers send data as bytes)
  b64_string = base64.b64encode(byte_creds).decode('utf-8')

  # Create the request with headers
  # Authorization: Basic bXlfY2xpZW50X2lkOm15X3NlY3JldF9wYXNzd29yZA==

  headers = {
    "Authorization": f'Basic {b64_string}',
    # 'Content-Type' is not included here, but Spotify defaults it for us
    # WE could also explicitly add it: 'Content-Type':'application/x-www-form-urlencoded'
  }

  # Create the body for the request
  # 'grant_type' tells Spotify what kind of token we want
  # For this app, we're using the 'client-credentials' method
  data = {
    'grant_type': 'client_credentials'
  }

  # Send a Post request to Spotify's token endpoint
  # - url:  where to send it
  # - headers: who's sending it (our credentials)
  # - data: what we're asking for
  response = requests.post(url, headers=headers, data=data)

  # If the request worked (status 200 = OK)
  # Spotify will send back some JSON data with our access token inside
  if response.status_code == 200:
    data = response.json()         #Converting response to Python Dictionary
    return data['access_token']    #Grab the token and return it
  else:
    print("Ran into an error when fetching token")

# print(get_token())

def search_song(title):
  '''Search a song by title'''

  # 1. Spotify search endpoint URL
  url = "https://api.spotify.com/v1/search"

  # 2. Parameters for the search request
  # 'q' = query string (the song title we want to search)
  # 'type' = specify we want to search for tracks (songs)
  # 'limit' = number of results we want back (1 means just the first result)
  params = {
    'q': title,
    'type': 'track',
    'limit': 1
  }

  # 3. Headers for the request
  # Authorization header is required to prove we have permission to access Spotify API
  # get_token() is a function that returns our Spotify access token
  headers = {
    "Authorization": f"Bearer {get_token()}"
  }

  # 4. Send a GET request to the Spotify API
  # We include the URL, headers (for auth), and parameters (search query)
  response = requests.get(url, params=params, headers=headers)
  
  # 5. Check if the request was successful (status code 200 means OK)
  if response.status_code == 200:
    # Convert the response from JSON format into a Python dictionary
    data = response.json()
    print(json.dumps(data, indent=2))

    # 6. Print some key details from the first track result
    # Artist name
    print(data["tracks"]["items"][0]["artists"][0]['name'])
    # Album name
    print(data["tracks"]["items"][0]["album"]["name"])
    # Album cover image URL
    print(data["tracks"]["items"][0]["album"]["images"][0]['url'])
    # Song name
    print(data["tracks"]["items"][0]["name"])

search_song("Ride the lightning")