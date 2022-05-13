from os import getenv
import requests
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates


KEY = getenv('YOUTUBE_API_KEY')
YOUTUBE_URL = 'https://www.googleapis.com/youtube/v3/search'

app = FastAPI()


templates = Jinja2Templates(directory='templates')


@app.get("/ok")
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


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request' : request, 'id': 1})

