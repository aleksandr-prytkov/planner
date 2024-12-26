from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.events import Event


class User(BaseModel):
    email: EmailStr
    password: str
    events: Optional[List[Event]] = None

    class Config:
        json_schema_extra = {
            "example": {
                "email": "example@email.com",
                "password": "strong!!!",
                "events": [],
            }
        }


class NewUser(User):
    def __eq__(self, other):
        if isinstance(other, NewUser):
            return self.email == other.email
        return False

    def __hash__(self):
        return hash(self.email)


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "example@email.com",
                "password": "strong!!!",
                "events": [],
        }
}