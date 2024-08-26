""""This is the main file of the project. It contains the FastAPI app and
imports all the routes from the modules folder.
"""

import importlib

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import src.modules as routes

app = FastAPI(
    swagger_ui_parameters={
        "syntaxHighlight.theme": "obsidian",
        "docExpansion": "list",
        "filter": True,
    }
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
for route in routes.modules:
    module = importlib.import_module(f"src.modules.{route}.routes")
    app.include_router(module.router, prefix="/api")
