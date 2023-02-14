# team-management-app

A simple Team Management Web application built with Django.
This task was given as a take-home assignment where I spent approximately 15 hours.

## TODO

### Features

- [x] Users can browse a list of team members
- [x] Users can browse details of one team member
- [x] Users can edit information of a team member
- [x] Users can add a new team member
- [x] Users can delete an existing team member

### Others

- [x] Write unit tests for models, views, adn forms.
- [x] Write integration test to verify the behavior of the core functionalities.

## How to install and run this app locally

**For the security of the application, SECRET_KEY is not included in this repository.**

**For those interested in running locally, please feel free to contact me.**

1. Navigate to the project directory

2. Make sure to place .env file under the root directory from here: https://upload.disroot.org/r/R8UJXZup#yFGr/IPFicNyiEcgxEDwMLTcNrSFTp6pnyR57f0VIPM=

3. Create a virtual environment (* Need to install virtualenv via pip before)

```
virtualenv env
```

```
source env/bin/activate
```

4. Install all dependencies specified in requirements.txt

```
pip install -r requirements.txt
```

5. Set up the DB with model schemas

```
python manage.py migrate
```

6. Spin up the server

```
python3 manage.py runserver
```

7. Open up http://localhost:8000/

## How to run Unit Test and Integration Test

First. spin up the server with tests database by specifying the env variable.

```
DJANGO_DATABASE='tests' python3 manage.py runserver
```

The following command will run both unit tests and integration tests.

```
python3 manage.py test
```

### What IntegrationTest using Selenium tests

- Users can see a list of teammembers to users
- Users can add a new member and see it in the list
- Users can edit an existing member and see instant changes
- Users can delete an existing member

