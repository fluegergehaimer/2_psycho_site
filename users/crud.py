from .shemas import CreateUser


def create_user(user_input: CreateUser) -> dict:
    user = user_input.model_dump()
    return {
        "success": True,
        "user": user
    }
