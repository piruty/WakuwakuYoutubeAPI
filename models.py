from typing import List
from pydantic import BaseModel


class PageInfo(BaseModel):
    totalResults: int
    resultsPerPage: int


class Id(BaseModel):
    kind: str
    videoId: str


class Thumbnail(BaseModel):
    url: str
    width: int
    height: int


class Thumbnails(BaseModel):
    default: Thumbnail
    medium: Thumbnail
    high: Thumbnail


class Snippet(BaseModel):
    publishedAt: str
    channelId: str
    title: str
    description: str
    thumbnails: Thumbnails
    channelTitle: str
    liveBroadcastContent: str
    publishTime: str


class Item(BaseModel):
    kind: str
    etag: str
    id: Id
    snippet: Snippet


class DataAPIResponse(BaseModel):
    kind: str
    etag: str
    nextPageToken: str
    regionCode: str
    pageInfo: PageInfo
    items: List[Item]
