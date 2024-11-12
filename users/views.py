from fastapi import APIRouter

from .shemas import CreateUser
from users import crud


router = APIRouter(prefix="/users", tags=["Пользователи"])


@router.post("/")
def create_user(user: CreateUser):
    return crud.create_user(user_input=user)

