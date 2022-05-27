
from re import templates
from typing import Union
from urllib import response
from urllib.request import Request

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app=FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def read_root():
    return{"Stiven": "Pinilla"}
async def read_item(request: Request):
    return templates.TemplateResponse("item.html")


