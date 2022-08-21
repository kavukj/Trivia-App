import json
import unittest
from flask import Flask
import unittest
from flaskr import create_app
from models import setup_db, Question


class TriviaTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database = "postgresql://jaink:Kavya1998@localhost:5432/trivia_test"
        setup_db(self.app,self.database)

    def tearDown(self):
        pass

    #Get question 
    def test_get_questions(self):
        res = self.client().get("http://127.0.0.1:5000/questions")
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['questions'])
        self.assertEqual(data['current_category'],None)
        self.assertEqual(len(data['categories']),6)

    def test_no_questions(self):
        res = self.client().get("http://127.0.0.1:5000/questions?page=1000")
        data = json.loads(res.data)
        self.assertEqual(res.status_code,400)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'],"Cannot Process request")

    #Get Question by category
    def test_get_question_by_category(self):
        res = self.client().get("/categories/2/questions")
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['current_category'],"Arts")
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['questions'])

    def test_get_question_invalid_category(self):
        res = self.client().get("/categories/0/questions")
        data = json.loads(res.data)
        self.assertEqual(res.status_code,400)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'],"Cannot Process request")

    #Create Questions
    def test_create_question(self):
        res = self.client().post("/questions",json={'question':'Where is Taj Mahal?','answer':'Agra','difficulty':'2','category':4})
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)

    def test_create_question_with_no_data(self):
        res=self.client().post("/questions")
        data = json.loads(res.data)
        self.assertEqual(res.status_code,400)
        self.assertEqual(data['message'],'Cannot Process request')

    #Delete Questions
    def test_delete_question(self):
        res=self.client().delete("/questions/11")
        data = json.loads(res.data)
        question = Question.query.filter(Question.id==4).one_or_none()
        self.assertEqual(question,None)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertEqual(len(data['categories']),6)
        self.assertEqual(data['current_category'],None)
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'])

    def test_delete_wrong_question(self):
        res=self.client().delete("/questions/10")
        data = json.loads(res.data)
        self.assertEqual(res.status_code,500)
        self.assertEqual(data['message'],"Internal Server Error")
        self.assertEqual(data['error'],500)

if __name__ == "__main__":
        unittest.main()
