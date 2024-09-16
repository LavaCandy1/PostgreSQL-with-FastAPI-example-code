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
2. Install the required Python packages:
3. Set up a PostgreSQL database:
   - Make sure you have PostgreSQL installed and running.
   - Create a database called QuizApp.
   - Update the URL_DATABASE in database.py with your PostgreSQL username, password, and database name:
     ```plaintext
     URL_DATABASE = "postgresql://<username>:<password>@localhost:5432/QuizApp"
     ```
4. Run the FastAPI application:
   - uvicorn main:quiz --reload
