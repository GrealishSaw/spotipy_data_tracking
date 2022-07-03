import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time
import data


client_id = data.client_id
client_secret = data.client_sec

uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'


client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

playlist = sp.artist_top_tracks(uri)

print(playlist)
