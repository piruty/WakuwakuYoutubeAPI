from os import getenv

import requests
import click


YOUTUBE_URL = 'https://www.googleapis.com/youtube/v3/search'


@click.command()
@click.option('--key', type=str, default='', help='Youtube Key')
@click.option('--count', type=int, default=5, help='Result item count')
@click.option('--query', type=str, default='', help='Search Query')
def search_youtube(key: str, count: int, query: str):
    if key == '':
        key = getenv('YOUTUBE_API_KEY')

    payload = {
        'key': key,
        'part': 'snippet',
        'type': 'video',
        'maxResults': count,
        'order': 'videoCount'
    }

    if query != '':
        payload['q'] = query

    r = requests.get(YOUTUBE_URL, params=payload)
    click.echo(r.json())

if __name__ == '__main__':
    search_youtube()
