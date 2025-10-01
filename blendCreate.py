import tekore as tk
import random

from spotifyHelp import authorize, getPlaylistTracks

def autoGenerateBlend(destID, sourceIds, numSongsEach = 50):

    spotify = authorize()

    sources = []
    for sourceId in sourceIds:
        sources.append(getPlaylistTracks(spotify, sourceId))

    allSongs = [(song.track.uri,i) for i, source in enumerate(sources) for song in source]
    random.shuffle(allSongs)
    songsRem = [numSongsEach] * len(sources)
    finalSongs = []
    for t in allSongs:
        if songsRem[t[1]] > 0 and t[0] not in finalSongs:
            songsRem[t[1]] -= 1
            finalSongs.append(t[0])
        if sum(songsRem) == 0:
            break
    spotify.playlist_clear(destID)
    spotify.playlist_add(destID, finalSongs)
    