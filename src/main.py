""""This is the main file of the project. It contains the FastAPI app and
imports all the routes from the modules folder.
"""
import importlib

from fastapi import FastAPI

import src.modules as routes

app = FastAPI(
    swagger_ui_parameters={
        "syntaxHighlight.theme": "obsidian",
        "docExpansion": "list",
        "filter": True,
    }
)

for route in routes.modules:
    module = importlib
