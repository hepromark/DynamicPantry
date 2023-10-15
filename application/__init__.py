from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["SECRET_KEY"] = "5ff79d1f29b74c7c7c8df18cc40cfb7f491cd070"
app.config["MONGO_URI"] = "mongodb+srv://dynamicpantry:dynamicpantry123@dynamicpantry.olc67vp.mongodb.net/?retryWrites=true&w=majority"

# setup mongodb
mongodb_client = PyMongo(app)
db = mongodb_client.db

from application import routes