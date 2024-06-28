

# Django REST API Project for User, Client, and Project Management

This project implements a Django REST API for managing users, clients, and projects. It includes features for registering clients, retrieving client information, editing/deleting client information, adding new projects for clients, assigning users to projects, and retrieving projects assigned to logged-in users.

## Technologies Used

- Django
- Django REST Framework
- PostgreSQL

## Read Instructions

1. **Clone the repository:**
   ```sh
   git clone https://github.com/deadpool3v/nimap_project.git
   cd nimap_project

2. Navigate to machine_test directiory & setup the python env:
   ```sh
   python3 -m venv nimap_venv
   On Windows use `.\nimap_venv\Scripts\activate`
   cd machine_test
   pip install -r requirements.txt

3. Configure the database:
   ```sh
   Update the DATABASES setting in settings.py to point to your PostgreSQL database. 
      DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.postgresql',
              'NAME': 'database_name',
              'USER': 'username',
              'PASSWORD': 'your_password',
              'HOST': 'localhost',
              'PORT': '5432',
          }
      }
   use your database

4. Apply Migrations:
   ```sh

   python manage.py makemigrations
   python manage.py migrate

5. **Create a superuser (admin)**

6. **python manage.py runserver**


7. Testing
I have tested the API 
a. list of all clients.
   ```sh

   ![Screenshot 2024-06-28 133623](https://github.com/deadpool3v/nimap_project/assets/141556250/9689214d-c124-4b4c-aa0d-911469253f92)

b. Creating a new client.
   ```sh
    ![Screenshot 2024-06-28 134401](https://github.com/deadpool3v/nimap_project/assets/141556250/f27eaeb9-0941-4c60-ac7f-dc247e2dbb5f)

c. List of all projevts assigned to the logged-in user.
   ```sh
![Screenshot 2024-06-28 131727](https://github.com/deadpool3v/nimap_project/assets/141556250/dba16ba8-25e5-4050-b511-54311a6bf47a)

