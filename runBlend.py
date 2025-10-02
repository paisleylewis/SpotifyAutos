import sys
from blendCreate import autoGenerateBlend

blend_id = sys.argv[1]
user_playlist_ids = sys.argv[2:]

autoGenerateBlend(blend_id, user_playlist_ids)