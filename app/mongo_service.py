import bson
from flask_pymongo import PyMongo

from app import create_app

app = create_app()
mongo = PyMongo(app)

def get_categories():
    return mongo.db.categorias.find()

def get_business_by_type(category: str):
    return mongo.db.empresas.find({"type": category})

def get_business_information(id: str):
    return mongo.db.empresas.find_one({"_id": bson.ObjectId(oid=str(id))})