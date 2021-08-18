import unittest

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

@app.route('/business')
def business():
    business_categories = mongo.db.categorias.find()
    return render_template('categories.html', categories=business_categories )

@app.route('/business/<category>', methods=['GET'])
def category(category):
    business_category = mongo.db.empresas.find({"type": category})
    return render_template('business.html', enterprises=business_category)