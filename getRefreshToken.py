import tekore as tk
import os

client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv('SPOTIFY_SECRET')
redirect_uri = os.getenv('SPOTIFY_REDIRECT')

cred = tk.Credentials(client_id, client_secret, redirect_uri)
token = tk.prompt_for_user_token(client_id, client_secret, redirect_uri, scope=tk.scope.every)

# Print refresh token
# Must be added to Github Secrets to use
print(token.refresh_token)