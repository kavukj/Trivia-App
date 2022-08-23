import json
import unittest
from flask import Flask
import unittest
from flaskr import create_app
from models import setup_db, Question
from flask_sqlalchemy import SQLAlchemy


class TriviaTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database = "postgresql://jaink:Kavya1998@localhost:5432/trivia_test"
        setup_db(self.app,self.database)

        
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

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
        self.assertEqual(data['message'],"Bad Request")

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
        self.assertEqual(res.status_code,404)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'],"Page Not Found")

    #Create Questions
    def create_question(self):
        res = self.client().post("/questions",json={'question':'Where is Taj Mahal?','answer':'Agra','difficulty':'2','category':4})
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)

    def test_create_question_with_no_data(self):
        res=self.client().post("/questions")
        data = json.loads(res.data)
        self.assertEqual(res.status_code,400)
        self.assertEqual(data['message'],'Bad Request')

    #Delete Questions
    def delete_question(self):
        res=self.client().delete("/questions/15")
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

    #Search Questions
    def test_questions_with_search_value(self):
        res = self.client().post("/search",json={"searchTerm":"movie"})
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['questions'])
        self.assertEqual(data['total_questions'],1)

    def test_questions_with_wrong_search_parameter(self):
        res = self.client().post("/search",json={"searc":"movie"})
        data = json.loads(res.data)
        self.assertEqual(res.status_code,404)
        self.assertEqual(data['error'],404)
        self.assertEqual(data['message'],"Page Not Found")

    #Quiz Cases
    def test_quiz_questions(self):
        res = self.client().post("/quizzes",json={'previous_questions': [],'quiz_category':'4'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['currentQuestion'])

    def test_quiz_questions_wrong_parameter(self):
        res = self.client().post("/quizzes",json={'questions': [],'quiz_category':4})
        data = json.loads(res.data)
        self.assertEqual(res.status_code,500)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'],'Internal Server Error')

if __name__ == "__main__":
        unittest.main()

