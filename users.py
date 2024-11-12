# from fastapi import APIRouter
# from pydantic import BaseModel, EmailStr


# router = APIRouter(prefix="/users", tags=["Пользователи"])


# class CreateUser(BaseModel):
#     login: str
#     email: EmailStr
#     password: int


# @router.post("/")
# def create_user(user: CreateUser):
#     return {
#         "message": "Success",
#         "email": user.email,
#     }
