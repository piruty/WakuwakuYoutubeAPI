from os import getenv

import requests

KEY = getenv('YOUTUBE_API_KEY')
YOUTUBE_URL = 'https://www.googleapis.com/youtube/v3/search'

payload = {
    'key': KEY,
    'part': 'snippet',
    'type': 'video',
    'maxResult': 5,
    'q': 'hikakin'
}

r = requests.get(YOUTUBE_URL, params=payload)
print(r.json())
