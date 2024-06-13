# EduWeb

EduWeb is an educational web application developed with Django that provides functionalities for user management, forums, and skills. The project includes an API documented using Swagger.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Routes](#api-routes)
- [API Documentation](#api-documentation)
- [Contributions](#contributions)

## Features

- User management with authentication.
- Discussion forums for users.
- Skill management.
- API documentation with Swagger.

## Technologies

- Python 3.12
- Django 5.0.6
- Django REST Framework
- drf-yasg (for API documentation)
- Poetry (for dependency management)

## Installation

### Prerequisites

- Python 3.12
- Poetry

### Installation Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/No-Country/c-18-52-t-python.git
    cd eduweb
    ```

2. Install the dependencies:

    ```bash
    poetry install
    ```

3. Create the `.env` file at the root of the project and add the necessary environment variables. You can base it on the `.env.example` file.

4. Run the database migrations:

    ```bash
    poetry run python manage.py migrate
    ```

5. Start the development server:

    ```bash
    poetry run python manage.py runserver
    ```

## Configuration

Make sure to configure the following variables in your `.env` file:

```env
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3
```


## Usage

- Admin Panel: http://localhost:8000/admin/

## API Documentation:
- Swagger UI: http://localhost:8000/swagger/
- ReDoc: http://localhost:8000/redoc/


## API Routes

- Users: /api/users/
- Forums: /api/forum/
- Skills: /api/skills/

## API Documentation


The API is documented using Swagger. You can access the documentation at:

- Swagger UI: http://localhost:8000/swagger/
- ReDoc: http://localhost:8000/redoc/


## Contributions
Contributions are welcome! Please fork the repository and submit a pull request.
