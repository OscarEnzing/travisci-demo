import unittest, json

from main import app


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_unauthorized(self):
        response = self.app.get('/authorized')
        # Check if the request fails with authorization error
        self.assertEqual(response._status_code,401,'Unauthorized access to page without login')

    def test_authorisation(self):
        response = self.app.get('/authorized')
        resp = response.data.decode('utf-8')
        self.assertEqual(resp, "You are logged in", 'login no work')

    def test_multiply(self):
        response = self.app.get('/multiply?x=5&y=7')
        resp = json.loads(response.data)
        self.assertEqual(resp['answer'],35,'Multiply endpoint failed known answer 7*5 = 35')

    def test_hello_world(self):
        response = self.app.get('/')
        resp = response.data.decode('utf-8')
        self.assertEqual(resp, "Hello World!", 'print not nice')

    def test_uppercase(self):
        response = self.app.get('/touppercase?s=pizza')
        resp = response.data.decode('utf-8')
        self.assertEqual(resp, "PIZZA", 'pizza not nice')


if __name__ == '__main__':
    unittest.main()
