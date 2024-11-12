from typing import Annotated

from fastapi import APIRouter, Path


router = APIRouter(prefix="/eating_disorder", tags=["РПП"])


@router.get("/")
def eating_disorder():
    return [
        "post1",
        "post2",
        "post3"
    ]


@router.get("/{post_id}")
def get_ed_post(post_id: Annotated[int, Path(ge=1)]):
    return {
        "post": {
            "id": post_id,
        },
    }
