from typing import List

from bson import ObjectId
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from pymongo.collection import Collection

from app.models import URL
from app.dependencies.mongodb import get_database
from app.collections import url
from app.utils.helper_functions import extract_uuid_from_short_url
from app.utils.ops import get_short_url

router = APIRouter()


class URLInput(BaseModel):
    url: str


class URLResponse(BaseModel):
    url: str


# Create an item
@router.post("/shorten/", response_model=URLResponse)
async def create_item(item: URLInput):
    original_url = item.url
    short_url = get_short_url()
    collection_obj = {
        "original_url": original_url,
        "short_url": short_url,
        "uuid": extract_uuid_from_short_url(short_url)
    }
    url.collection.insert_one(collection_obj)
    return URLResponse(url=short_url)


@router.get("/{uuid}")
async def read_item(uuid: str):
    item = url.collection.find_one({"uuid": uuid})
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return URLResponse(url=item.get('original_url'))
