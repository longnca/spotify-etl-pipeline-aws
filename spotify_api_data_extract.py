import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import boto3
from datetime import datetime

def lambda_handler(event, context):

    client_id = os.environ.get('client_id')
    client_secret = os.environ.get('client_secret')
    
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    playlists = sp.user_playlists('spotify')
    
    # Go to Spotify online and copy the link of a playlist
    # Assign it to a variable
    playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbKj23U1GF4IR"
    
    # Split the link into several parts and extract the last part (the URI of the playlist)
    playlist_URI = playlist_link.split("/")[-1]
    
    # Use playlist_tracks() method to extract information from the URI and store it into a variable
    spotify_data = sp.playlist_tracks(playlist_URI)
    
    client = boto3.client('s3')
    
    filename = "spotify_raw_" + str(datetime.now()) + ".json"
    
    client.put_object(
        Bucket= "spotify-etl-project-tutorial",
        Key= "raw_data/to_processed/" + filename,
        Body= json.dumps(spotify_data)
        )
