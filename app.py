from os import getenv
import requests
from fastapi import FastAPI


KEY = getenv('YOUTUBE_API_KEY')
YOUTUBE_URL = 'https://www.googleapis.com/youtube/v3/search'

app = FastAPI()


@app.get("/")
def ok():
    return 'ok'

@app.get("/youtube")
def search_youtube():
    payload = {
        'key': KEY,
        'part': 'snippet',
        'type': 'video',
        'maxResults': 5,
        'order': 'videoCount',
        'q': 'hikakin'
    }

    r = requests.get(YOUTUBE_URL, params=payload)
    return r.json()
