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

    if __name__ == "__main__":
        unittest.main()
