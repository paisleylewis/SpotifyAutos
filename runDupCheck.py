import sys
import spotifyHelp

playlistIds = sys.argv[1:]

spotify = spotifyHelp.authorize()

playlists = [spotifyHelp.getPlaylistTracks(spotify, playlistId) for playlistId in playlistIds]

print(spotifyHelp.dupcheck(playlists))

