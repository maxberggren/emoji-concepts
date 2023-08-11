from dotenv import load_dotenv

load_dotenv()

import os
import random
import stripe
import json5
from typing_extensions import Annotated
from fastapi import FastAPI, Request, Form, HTTPException, Depends, status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import List
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from uuid import uuid4
from data import concepts


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")
tr = templates.TemplateResponse


@app.get("/")
async def route(request: Request, search: str = None):
    if search:
        suggestions = [
            item
            for item in concepts
            if any(search.lower() in str(value.lower()) for value in item.values())
        ]
    else:
        suggestions = random.sample(concepts, 10)
    return tr(
        "search.html",
        {"request": request, "suggestions": suggestions, "n_concepts": len(concepts)},
    )


@app.get("/{search}/")
async def route(request: Request, search: str):
    search = search.replace("-", " ")
    suggestions = [
        item for item in concepts if search.lower() in item["concept"].lower()
    ]
    return tr(
        "search.html",
        {"request": request, "suggestions": suggestions, "n_concepts": len(concepts)},
    )
