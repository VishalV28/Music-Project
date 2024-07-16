import requests
import base64

# Spotify API credentials
client_id = '548c969142484272992729b78278aaa1'
client_secret = '0fb907075c9644409f9d7a2969703421'

# Function to get Spotify access token
def get_spotify_access_token(client_id, client_secret):
    url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': 'Basic ' + base64.b64encode(f"{client_id}:{client_secret}".encode()).decode(),
    }
    data = {
        'grant_type': 'client_credentials',
        'client_id': '548c969142484272992729b78278aaa1',
        'client_secret': 'fb907075c9644409f9d7a2969703421'
    }
    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        try:
            access_token = response.json()['access_token']
            return access_token
        except KeyError:
            print("Error: 'access_token' key not found in response JSON.")
            print(response.json())
            return None
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

# Get Spotify access token
access_token = get_spotify_access_token(client_id, client_secret)

if access_token:
    print(f"Successfully obtained access token: {access_token}")
else:
    print("Failed to obtain Spotify access token.")