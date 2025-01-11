from fastapi import APIRouter, Body, HTTPException, status, Depends
from models.events import Event
from typing import List, Annotated

event_router = APIRouter(
    tags=["Events"]
)

events = []


@event_router.get("/", response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    return events


@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: int) -> Event:
    for event in events:
        if event.id == id:
            return event
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )


@event_router.post(
    "/new",
    summary="Создать новое событие",
    response_description="Сообщение об успешном создании события"
)
async def add_event(body: Annotated[Event, Body(..., description="Данные события")]) -> dict:
    events.append(body)
    return {
        "message": "Event created successfully"
    }


@event_router.delete("/{id}")
async def delete_event(id: int) -> dict:
    for event in events:
        if event.id == id:
            events.remove(event)
            return {"message": "Event deleted successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )


@event_router.delete("/")
async def delete_all() -> dict:
    events.clear()
    return {
        "message": "Events deleted successfully"
    }
