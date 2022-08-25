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
    $env:FLASK_APP=flaskr
    $env:FLASK_ENV=development
    flask run
    ```

3. If you are on mac:
    ```
    export FLASK_APP = flaskr
    export FLASK_ENV = development
    flask run
    ```

#### Note: Make sure to run the flask run command from backend directory and not inside flaskr directory.

These commands will redirect our application use `__init.py` and load the server. The server runs on `http://127.0.0.1:5000/` by default. When we open this URL, the application will redirect to index.

### Frontend

For the frontend dependencies, we have a file named package.json where all the dependencies are mentioned. We need to install them.
to install them run the command from frontend folder:

    ```
    npm install
    ```

To start the frontend application, run:

    ```
    npm run start
    ```

By default, the frontend local runs on port 3000. i.e. `http://localhost:3000/`

## Tests



