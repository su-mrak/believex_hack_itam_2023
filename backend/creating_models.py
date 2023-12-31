from datetime import datetime

from pydantic import BaseModel, Field
from test_objects import *


# REQUEST MODELS:
# # add model_config to generate schema


class UserCreateRequest(BaseModel):
    username: str = Field(example="sab_boy")
    password: str = Field(example="0000000")  # add check for requirements
    status: str = Field(example="admin")
    name: str | None = Field(..., example="Арсений Синицын")
    social_networks: dict | None = Field(..., example=social_networks)
    stack: set[str] | None = Field(..., example=stack)
    tags: set[str] = Field(default=[], example=tags)
    image: bytes | None = None
    description: str | None = Field(..., example="I wish u best but I'm the best.")


class TeamCreateRequest(BaseModel):
    team_name: str = Field(..., example="BelieveX")
 
    members: set[int] = Field(
        ...,
        example=(22, 1, 3, ),
    )  # usernames, no captain, only other members
    capitan: int = Field(..., example="23")  # take user id who created team
    image: bytes | None = None
    description: str | None = None


class HackCreateRequest(BaseModel):
    id: int = Field(..., example=1)
    name: str = Field(..., example="LCT 2023 Moscow ")
    website_link: str = Field(..., example="https://leaders2023.innoagency.ru/")
    registration_link: str | None = Field(example=None)
    registration_started_at: datetime | None = Field(
        ..., example=datetime(2023, 4, 23, 00, 00, 00, 0)
    )
    registration_ended_at: datetime = Field(
        ..., example=datetime(2023, 6, 23, 00, 00, 00, 0)
    )
    event_started_at: datetime | None = Field(
        ..., example=datetime(2023, 10, 18, 00, 00, 00, 0)
    )
    event_ended_at: datetime | None = Field(
        ..., example=datetime(2023, 10, 21, 00, 00, 00, 0)
    )
    format: str = Field(..., example="online")
    city: str | None = Field(..., example="Moscow")  # can be more than one city ???
    prize: str | None = Field(..., example="$1000")
    team_members_number_min: int | None = Field(..., example=2)
    team_members_number_max: int = Field(..., example=5)
    tags: set[str] | None = Field(..., example=["ml", "design"])
    description: str = Field(..., example="")



class PublicationCreateRequest(BaseModel):
    title: str = Field(..., example="How to make layout design for 3 days?")
    inner_link: bool
    url: str | None = Field(..., example=None)
    publication_type: str = Field(..., example="git repo")
    tags: set[str] | None = Field(..., example=("ml",))
    created_by: int = Field(..., example=42)
    created_at: datetime | None = Field(
        ..., example=datetime(2022, 10, 21, 00, 00, 00, 0)
    )
    description: str = Field(..., example="cool description")
