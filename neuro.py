from typing import Annotated

from fastapi import APIRouter, Path


router = APIRouter(prefix="/neuro", tags=["Нейро"])


@router.get("/")
def neuro_page():
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
