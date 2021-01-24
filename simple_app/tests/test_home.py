import unittest
from simple_app.app import app as tested_app
import json

class TestedApp(unittest.TestCase):
    def test_home(self):

        #creating a client to help get the app tested

        app=tested_app.test_client()

        hello=app.get('/api') # calling the /api endpoint

        #assert the body
        body=json.loads(str(hello.data,'utf-8'))


        self.assertEqual(body['message'],"Hello")

    def test_api_user(self):
        app=tested_app.test_client()

        hello_user=app.get('/api/user')

        body=json.loads(str(hello_user.data,'utf-8'))

        self.assertEqual(body['Hello'],"Anonymous")

if __name__ == "__main__":
    unittest.main()