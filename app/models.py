from pydantic import BaseModel


class URL(BaseModel):
    original_url: str
    uuid: str
    short_url: str


class UsedIdentifiers(BaseModel):
    uuid: str
