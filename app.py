from os import getenv
import requests
from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from models import DataAPIResponse


KEY = getenv('YOUTUBE_API_KEY')
YOUTUBE_URL = 'https://www.googleapis.com/youtube/v3/search'

app = FastAPI()


templates = Jinja2Templates(directory='templates')


@app.get("/ok")
def ok():
    return 'ok'

@app.get("/youtube")
def search_youtube(request: Request):
    payload = {
        'key': KEY,
        'part': 'snippet',
        'type': 'video',
        'maxResults': 5,
        'order': 'videoCount',
        'q': 'hikakin'
    }

    r = requests.get(YOUTUBE_URL, params=payload)
    if r.status_code != 200:
        raise HTTPException(status_code=403, detail='Bad Request')

    response = DataAPIResponse.parse_obj(r.json())
    return templates.TemplateResponse('youtube_list.html', {'request': request, 'items': response.items})


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request' : request, 'id': 1})

