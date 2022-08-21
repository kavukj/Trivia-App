from unicodedata import category
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginate(request,questions):
    page = request.args.get('page',1,type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    format_questions = [question.format() for question in questions]
    return format_questions[start:end]

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    cors = CORS(app, resources={r'*': {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        return response

    @app.route("/")
    def index():
        return "Hello"

    '''Route to Get all questions'''
    @app.route("/questions",methods=["GET"])
    def get_questions():
        questions = Question.query.order_by(Question.id).all()
        categories = Category.query.all()
        format_categories = [category.format() for category in categories]
        paginate_question = paginate(request,questions)
        if len(paginate_question) > 0:
            return jsonify({
                'success':True,
                'questions':paginate_question,
                'total_questions':len(questions),
                'categories':format_categories,
                'current_category':None
            })  
        else:
            abort(400)  

    '''Route to delete a question'''
    @app.route("/questions/<id>",methods=['DELETE'])
    def delete_question(id):
        try:
            question = Question.query.filter(Question.id==id).one_or_none()
            if question is None:
                abort(404)
            else:
                question.delete()
                questions = Question.query.order_by(Question.id).all()
                categories = Category.query.all()
                format_categories = [category.format() for category in categories]
                paginate_question = paginate(request,questions)
                if len(paginate_question) > 0:
                    return jsonify({
                    'success':True,
                    'questions':paginate_question,
                    'total_questions':len(questions),
                    'categories':format_categories,
                    'current_category':None
                })
        except:
            abort(500)

    '''Route to create new question'''
    @app.route("/questions",methods=['POST'])
    def create_question():
        body = request.get_json()
        question = body.get('question',None)
        answer = body.get('answer',None)
        difficulty = body.get('difficulty',None)
        category=body.get('category',None)

        try:
            question = Question(question=question,answer=answer,difficulty=difficulty,category=category)
            question.insert()
            return jsonify({
                'success':True
            })
        except:
            abort(500)
    """
    @TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """

    '''Route to Get all categories'''
    @app.route('/categories')
    def categories():
        data = Category.query.all()
        categories = {}
        for category in data:
            categories[category.id] = category.type

        return jsonify({
            'categories': categories
        })

    '''Route to Get all question for a specific category'''
    @app.route("/categories/<id>/questions",methods=["GET"])
    def get_category_questions(id):
        try:
            questions = Question.query.filter(Question.category == id).order_by(Question.id).all()
            category = Category.query.filter(Category.id == id).with_entities(Category.type).one_or_none()
            format_questions = paginate(request,questions)
            print(category[0])
            return jsonify({
                'success':True,
                'questions':format_questions,
                'current_category':category[0],
                'total_questions':len(questions)
            })
        except:
            abort(404)

    """
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """

    @app.errorhandler(400)
    def bad_request(error):
         return jsonify({
            "success": False, 
            "error": 400,
            "message": "Bad Request"
            }), 400
    
    @app.errorhandler(500)
    def server_error(error):
         return jsonify({
            "success": False, 
            "error": 500,
            "message": "Internal Server Error"
            }), 500

    @app.errorhandler(404)
    def not_found(error):
         return jsonify({
            "success": False, 
            "error": 404,
            "message": "Page Not Found"
            }), 404

    @app.errorhandler(422)
    def unproccesable(error):
         return jsonify({
            "success": False, 
            "error": 422,
            "message": "Cannot Process Request"
            }), 422


    return app

