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

##Requirements
- Python 3.8 or higher
- PostgreSQL 12 or higher
