import json
import unittest
from flask import Flask
import unittest

from flaskr import create_app
from models import setup_db


class TriviaTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database = "postgresql://jaink:Kavya1998@localhost:5432/trivia_test"
        setup_db(self.app,self.database)

    def tearDown(self):
        pass

    def test_get_questions(self):
        res = self.client().get("http://127.0.0.1:5000/questions")
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['total_questions'])
        self.assertEqual(len(data['categories']),6)

    def test_no_questions(self):
        res = self.client().get("http://127.0.0.1:5000/questions?page=1000")
        data = json.loads(res.data)
        self.assertEqual(res.status_code,400)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'],"Cannot Process request")

if __name__ == "__main__":
        unittest.main()
