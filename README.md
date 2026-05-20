# Book Review API
A RESTful API project built using Django and Django REST Framework.

This project allows users to manage books and reviews with authentication features such as login and password changing.

## Features
- User Authentication
- Create Books
- Add Reviews
- Update and Delete Data
- Change Password Functionality Django
- Admin Panel
- REST API Support
## Technologies Used
- Python
- Django
- Django REST Framework
- SQLite
- Django Admin Interface
## Installation
Clone the repository:

bash git clone  https://github.com/FarahAlshammari/book-review-api.git

## Move to the project folder:
- cd book-review-api

## Install dependencies: 
- pip install -r requirements.txt

## Apply migrations:
- python manage.py migrate

## Create superuser:
- python manage.py createsuperuser

## Run the server:
- python manage.py runserver

## API Endpoints
Books

- /api/books/

Reviews

- /api/reviews/

Authentication

- /api-auth/login/

- /change-password/

## Admin Panel
The project uses a customized Django admin interface for a modern and responsive design.

- Admin URL: /admin/

## Project Status
Project completed successfully and tested using Django REST Framework