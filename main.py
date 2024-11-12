from typing import Annotated

from fastapi import FastAPI, Path
import uvicorn
from neuro.views import router as router_neuro
from eating_disorder.views import router as router_ed
from space.views import router as router_space
from users.views import router as router_users


app = FastAPI()
app.include_router(router_neuro)
app.include_router(router_ed)
app.include_router(router_space)
app.include_router(router_users)


@app.get("/")
def homepge():
    return {"message": "Homepage", }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
