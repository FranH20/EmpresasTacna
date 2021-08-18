from flask import Flask, app
from .config import MONGO_URI

def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = MONGO_URI
    return app
