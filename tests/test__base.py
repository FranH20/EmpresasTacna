from flask_testing import TestCase
from flask import current_app, url_for
from main import app

class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True 
        app.config['WTF_CSRF_ENABLED'] = False
        return app
    
    def test_app_exist(self):
        self.assertIsNotNone(current_app)
    
    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])
    
    def test_home_connection(self):
        response = self.client.get(url_for('index'))
        self.assert200(response)

    def test_business_connection(self):
        response = self.client.get(url_for('business'))
        self.assert200(response)
    
    def test_category_connection(self):
        response = self.client.get(url_for('business_category', category="comida"))
        self.assert200(response)
    
    def test_info_business_connection(self):
        response = self.client.get(url_for('business_information', category="comida", id="611beb5140dd8b71ba89ad0a"))
        self.assert200(response)