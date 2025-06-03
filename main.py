from fastapi import FastAPI, Request
from .models import Base
from .database import engine

from .routers import auth,todos
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
app=FastAPI()

Base.metadata.create_all(bind=engine)

templates=Jinja2Templates(directory="TodoApp/templates")

app.mount("/static", StaticFiles(directory="TodoApp/static"), name="static")

@app.get("/")
def test(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
app.include_router(auth.router)
app.include_router(todos.router)

