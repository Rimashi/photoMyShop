from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter(
    prefix="/pages",
    tags=["pages"],
)

templates = Jinja2Templates(directory="views")


@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/base", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})
