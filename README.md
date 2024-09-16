# FastAPI Quiz Application

This is a simple quiz application built with FastAPI and PostgreSQL. It allows you to create and retrieve quiz questions and choices, storing them in a PostgreSQL database.

## Features

- Create and save quiz questions and choices.
- Retrieve questions and associated choices by their unique IDs.
- PostgreSQL integration for database storage.

## Project Structure

```plaintext
├── main.py            # FastAPI application entry point
├── models.py          # SQLAlchemy models for questions and choices
├── database.py        # Database connection and session management
```

## Requirements
- Python 3.8 or higher
- PostgreSQL 12 or higher


## Installation
1. Clone this repository:
   ```
   git clone https://github.com/your-username/quiz-app.git
   cd quiz-app
   ```

2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```
3. Set up a PostgreSQL database:
   - Make sure you have PostgreSQL installed and running.
   - Create a database called QuizApp.
   - Update the URL_DATABASE in database.py with your PostgreSQL username, password, and database name:
     ```
     URL_DATABASE = "postgresql://<username>:<password>@localhost:5432/QuizApp"
     ```
     Replace {username}, {password}, and QuizApp with your PostgreSQL credentials.
4. Run the FastAPI application:
   ```
   uvicorn main:quiz --reload
   ```

## API Endpoints
1. Create a Quiz Question - "/questions/" ~ POST method
2. Retrieve a Quiz Question - "/get-question/{question_id}" ~ GET method
3. Retrieve Choices for a Question - "/get-choice/{choice_id}" ~ GET method

## Database Setup
Make sure to have PostgreSQL installed and running. The database connection URL is defined in database.py as:
```
URL_DATABASE = "postgresql://<username>:<password>@localhost:5432/QuizApp"
```


## Dependencies
Install dependencies by running:
*pip install -r requirements.txt*


This `README.md` covers installation, usage, and project structure, along with example API requests and responses. Let me know if you have any queries.

