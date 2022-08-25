# Trivia App

This project is a quiz game where you can increase you general knowledge and have fun. You can view multiple questions from a list of categories available to the user and also create questions on your own for all the categories available.
You can also play the trivia quiz and check your knowledge for different categories. When given wrong answer, you will be prompted with correct answer. You can play the quiz for any number of times with all or any one category.  

All backend code follows PEP8 style guidelines and frontend follows ES6 pattern.

## Getting Started

### Pre Requisites and Local Develpoment

Developers working on this project should have python3, pip and node installed on  their system.

### Backend

To start working on the backend folder for this project, you need to install all the dependencies which are mentioned in file requirement.txt within the backend folder. Run this command to install all dependencies:
    pip install requirement.txt

Once the installations are done, run following command to run the backend server on your system in development environment.
1. If you are on windows cmd:
    ```
    set FLASK_APP= flaskr
    set FLASK_ENV = development
    flask run
    ```

2. If you are on linux:
    ```
    $env:FLASK_APP="flaskr"
    $env:FLASK_ENV="development"
    flask run
    ```

3. If you are on mac:
    ```
    export FLASK_APP = flaskr
    export FLASK_ENV = development
    flask run
    ```

##### Note: Make sure to run the flask run command from backend directory and not inside flaskr directory.

These commands will redirect our application use `__init.py` and load the server. The server runs on `http://127.0.0.1:5000/` by default. When we open this URL, the application will redirect to index.

The backend directory structure follows a model.py file where all the database and table creations are written. The route controllers are written inside the init.py file.

For application backend handling, we need to setup the database and table. For this purpose, run following command:

    ```
    dropdb fsnd
    createdb fsnd
    psql fsnd < trivia.psql
    ```
##### Note: Omit dropdb command if running the project for the first time. You can change the database name as per your convinience. Make sure to make the reuqired changes in model.py file.

### Frontend

For the frontend we have used React.JS. We have a file named package.json where all the dependencies are mentioned to run the application locally. We need to install them.
To install the packages, run the command from frontend folder:

    ```
    npm install
    ```

To start the frontend application, run:

    ```
    npm run start
    ```

By default, the frontend local runs on port 3000. i.e. `http://localhost:3000/`

For frontend, all the styling related files are inside the stylesheets directory. the UI is divided into various components and there inside the directory named components.

## Tests

For this project, we also have a test file where test cases for all the routes are written. To run them successfully, we need to have our test database setup completed.
For this purpose, navigate to backend folder and run following commands:

    ```
    dropdb trivia_test
    createdb trivia_test
    psql trivia_test > trivia.psql
    ```

All the test cases are written in file named test_flaskr.py. All the test cases should be maintained with the latest updates as per the application functionality. To run the file:

    ```
    python test_flaskr.py
    ```

## API Reference

### Getting started
Current version of our project only works on local and is not hostel on any platform. 
- Base URL : The backend app is hosted at the default, `http://127.0.0.1:5000/`, which is set as a proxy in the frontend configuration.
- Authentication: Current version of our API's does not require any authentication or API keys or tokens.

### Error Handling
For our API's failing, a json object will be returned in following format:

```
response: {
    'success':False,
    'message':"Not Found",
    'error':400
}
```

Our API's will be returning four types of error on failure. They are:
    1. 404 - Cannot Process Request
    2. 400 - Bad Request
    3. 404 - Page Not Found
    4. 500 - Internal Server Error

### Error Handling

#### Get endpoints

1. GET /questions

- General:
    - Returns a list of all questions irrespective of any category with the response json containing total questions count, success value, array of all questions and all the categories.
- Sample:
    - curl http://127.0.0.1:5000/questions
- Response:
    ```
    {
        "categories": [
            {
                "id": 1,
                "type": "Science"
            },
            {
                "id": 2,
                "type": "Art"
            }
        ],
        "current_category": null,
        "questions": [
            {
                "answer": "Maya Angelou",
                "category": "4",
                "difficulty": 2,
                "id": 1,
                "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
            },
            {
                "answer": "Muhammad Ali",
                "category": "4",
                "difficulty": 1,
                "id": 2,
                "question": "What boxer's original name is Cassius Clay?"
            }
        ],
        "success": true,
        "total_questions": 2
    }
    ```

2. GET /categories

- General:
    - Returns a list of all categories with the response json containing all categories and success value.
- Sample:
    - curl http://127.0.0.1:5000/categories
- Response:
    ```
    {
        "categories": {
            "1": "Science",
            "2": "Art",
            "3": "Geography",
            "4": "History",
            "5": "Entertainment",
            "6": "Sports"
        },
        "success": true
    }
    ```

3. GET /categories/{id}/questions

- General:
    - Returns a list of all questions belonging to any selected category with the response json containing array of questions for that category, success value, total questions count and current category.
- Sample:
    - curl http://127.0.0.1:5000/categories/1/questions
- Response:
    ```
    {
        "current_category": "Science",
        "questions": [
            {
                "answer": "Mercury",
                "category": "1",
                "difficulty": 3,
                "id": 16,
                "question": "Hg is the chemical symbol of which element?"
            }
        ],
        "success": true,
        "total_questions": 1
    }
    ```

#### delete endpoints

1. DELETE /questions/{id}

- General:
    - Deletes the question based on question id given if it exists. After deleting the valid question, returns a json repsonse containing array of remaining questions, success value, total questions count and list of all categories.
- Sample:
    - curl http://127.0.0.1:5000/categories/1/questions -X DELETE
- Response:
    ```
    {
        "categories": [
            {
                "id": 1,
                "type": "Science"
            },
            {
                "id": 2,
                "type": "Art"
            },
            {
                "id": 3,
                "type": "Geography"
            },
            {
                "id": 4,
                "type": "History"
            },
            {
                "id": 5,
                "type": "Entertainment"
            },
            {
                "id": 6,
                "type": "Sports"
            }
        ],
        "current_category": null,
        "questions": [
            {
                "answer": "Maya Angelou",
                "category": "4",
                "difficulty": 2,
                "id": 1,
                "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
            }
        ],
        "success": true,
        "total_questions": 1
    }
    ```

#### post endpoints

1. POST /questions

- General:
    - Creates a new question using the submitted question, answer and category and difficulty level with the response json containing success value.
- Sample:
    - curl http://127.0.0.1:5000/questions -X POST -H "Content-Type:application/json" -d '{"question":"Where is Taj Mahal situated?","answer":"Agra","difficulty":2,"category":4}'
- Response:
    ```
    {
        "success": true,
    }
    ```

2. POST /search

- General:
    - Searches for a list of questions based on the search term provided with the response json containing array of all questions matching the searc term, success value, total questions count and list of all categories.
- Sample:
    - curl http://127.0.0.1:5000/search -X POST -H "Content-Type:application/json" -d '{"searchTerm":"Taj"}'
- Response:
    ```
    {
        "categories": [
            {
                "id": 1,
                "type": "Science"
            },
            {
                "id": 2,
                "type": "Art"
            }
        ],
        "current_category": null,
        "questions": [
            {
                "answer": "Agra",
                "category": "3",
                "difficulty": 2,
                "id": 11,
                "question": "The Taj Mahal is located in which Indian city?"
            },
            {
                "answer": "Agra",
                "category": "4",
                "difficulty": 2,
                "id": 22,
                "question": "Where is Taj Mahal situated?"
            }
        ],
        "success": true,
        "total_questions": 2
    }
    ```


3. POST /quizzes

- General:
    - Returns a random question based on the category id given with a response json containing a success value and currentQuestion.
- Sample:
    - curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type:application/json" -d '{"quiz_category":"1","previous_questions":[]}'
- Response:
    ```
    {
        "currentQuestion": {
            "answer": "Mercury",
            "category": "1",
            "difficulty": 3,
            "id": 16,
            "question": "Hg is the chemical symbol of which element?"
        },
        "success": true
    }
    ```

## Deployment

N/A. 
We do not have our project deployed.

## Author
Kavya Jain

## Acknowledgments
Would like to thank Udacity mentors.