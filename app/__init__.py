# Modules
from flask import Flask

# Initialization
app = Flask(
    "Bravo Company Seals",
    template_folder = "app/templates"
)

# Routes
from .routes import *
