import tekore as tk
import os
from dotenv import load_dotenv

def authorize():
    # Load .env only if running locally
    if os.getenv('GITHUB_ACTIONS') != 'true':
        load_dotenv()
    client_id = os.getenv('SPOTIFY_CLIENT_ID')
    client_secret = os.getenv('SPOTIFY_SECRET')
    redirect_uri = os.getenv('SPOTIFY_REDIRECT')
    refresh_token = os.getenv('SPOTIFY_REFRESH')

    cred = tk.Credentials(client_id, client_secret, redirect_uri)
    token = cred.refresh_user_token(refresh_token)
    spotify = tk.Spotify(token)
    return spotify

def getPlaylistTracks(spotify, playlistId):
    offset = 0
    fullsongsdetails = []
    while len(fullsongsdetails) == offset:
        tracks = spotify.playlist_items(playlistId,offset=offset).items
        for track in tracks:
            fullsongsdetails.append(track)
        offset += 100
    return fullsongsdetails
