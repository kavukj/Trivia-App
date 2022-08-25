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

All the test cases are written in file named test_flaskr.py. All the test cases should be maintained with the latest updates as per the application functionality. To run the file,
    ```
    python test_flaskr.py
    ```




