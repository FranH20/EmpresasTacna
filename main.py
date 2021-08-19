import unittest
import bson
    
from flask import render_template
from flask_pymongo import PyMongo

from app import create_app

app = create_app()
mongo = PyMongo(app)

@app.cli.command()
def test():    
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@app.route('/index')
@app.route('/')
def index():
    return render_template('home.html')

def item_information(category, id):
    business_information = mongo.db.empresas.find_one({"_id": bson.ObjectId(oid=str(id))})
    print(business_information)
    return render_template('item.html', b_info=business_information)

def item_business(category):
    business_category = mongo.db.empresas.find({"type": category})
    return render_template('business.html', enterprises=business_category)

def business():
    business_categories = mongo.db.categorias.find()
    return render_template('categories.html', categories=business_categories )

app.add_url_rule('/business', 'business', business)
app.add_url_rule('/business/<category>', 'business_category', item_business)
app.add_url_rule('/business/<category>/<id>', 'business_information', item_information)
