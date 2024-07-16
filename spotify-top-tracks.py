#

import requests
import pandas as pd

# Replace 'your_access_token' with the actual access token you obtained
access_token = 'BQA6gvIOBLgr3vXh6lQRp5YUd4NOE4SKbJmKj7vH_wHxzmvWUcYW24Q0yuvtl-_W4sjAS6FOigv8H6UjFWoV9wuoDh8c64VelP4wqILWrYqguCImGHQ'

# Function to get Spotify Top Tracks
def get_spotify_top_tracks():
    url = "https://api.spotify.com/v1/playlists/37i9dQZEVXbMDoHDwVN2tF/tracks"
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}, {response.json()}")
        return None

# Fetch Spotify Top Tracks data
spotify_top_tracks_data = get_spotify_top_tracks()

# Process and store the data if fetched successfully
if spotify_top_tracks_data:
    tracks = spotify_top_tracks_data['items']
    data = []
    for item in tracks:
        track = item['track']
        track_name = track['name']
        artist_name = ', '.join([artist['name'] for artist in track['artists']])
        album_name = track['album']['name']
        release_date = track['album']['release_date']
        track_popularity = track['popularity']
        data.append([track_name, artist_name, album_name, release_date, track_popularity])

    # Convert to DataFrame
    df = pd.DataFrame(data, columns=['Track Name', 'Artist', 'Album', 'Release Date', 'Popularity'])
    print(df.head())

    # Save DataFrame to a CSV file
    df.to_csv('spotify_top_tracks.csv', index=False)
else:
    print("Failed to fetch Spotify Top Tracks data.")
