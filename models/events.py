from pydantic import BaseModel, Field
from typing import List


class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        json_schema_extra = {
            "example": {
                "title": "My First Event",
                "image": "https://myimage.com/picture.png",
                "description": "My description for my first event",
                "tags": ["python", "fastapi", "launch"],
                "location": "Google meeting"
            }
        }