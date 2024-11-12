from typing import Annotated

from fastapi import APIRouter, Path


router = APIRouter(prefix="/space", tags=["Энергетика"])


@router.get("/")
def space():
    return [
        "post1",
        "post2",
        "post3"
    ]


@router.get("/{post_id}/")
def get_neuro_post(post_id: Annotated[int, Path(ge=1)]):
    return {
        "post": {
            "id": post_id,
        },
    }
