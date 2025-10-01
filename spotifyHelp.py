import tekore as tk
import os

def authorize():
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
    cur = 0
    while len(fullsongsdetails) == cur*100:
        myplaylist2 = spotify.playlist_items(playlistId,offset=offset)
        tracks2 = myplaylist2.items
        for track in tracks2:
            fullsongsdetails.append(track)
        cur+=1    
        offset += 100
    return fullsongsdetails
