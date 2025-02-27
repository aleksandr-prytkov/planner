from fastapi import APIRouter, HTTPException, status, Depends, Body
from models.users import NewUser, UserSignIn
from typing import Annotated


user_router = APIRouter(
    tags=["User"]
)

users = {}


@user_router.post("/signup")
async def sign_new_user(
        data: Annotated[
            NewUser,
            Body(...)
        ]
) -> dict:
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied username exists"
        )

    users[data.email] = data
    return {
        "message": "User successfully registered!"
    }


@user_router.post("/signin")
async def sign_user_in(
        user: Annotated[
            UserSignIn, Body(...)
        ]
) -> dict:
    if not users.get(user.email):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )
    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wrong credentials passed"
        )
    return {
        "message": "User signed in successfully"
    }
