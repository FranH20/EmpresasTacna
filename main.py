import unittest
from flask import render_template
from app.mongo_service import get_business_information, get_business_by_type, get_categories
from app import create_app

app = create_app()

@app.cli.command()
def test():    
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@app.route('/index')
@app.route('/')
def index():
    return render_template('home.html')

def item_information(category, id):
    business_information = get_business_information(id=id) 
    return render_template('item.html', b_info=business_information)

def item_business(category):
    business_category = get_business_by_type(category=category)
    return render_template('business.html', enterprises=business_category)

def business():
    business_categories = get_categories()
    return render_template('categories.html', categories=business_categories )

app.add_url_rule('/business', 'business', business)
app.add_url_rule('/business/<category>', 'business_category', item_business)
app.add_url_rule('/business/<category>/<id>', 'business_information', item_information)
