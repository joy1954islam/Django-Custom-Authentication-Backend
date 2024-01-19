# Opus Backend

Opus is a job portal for employers and candidates.

## Build with
* [Python v3.11](https://www.python.org/)
* [Django v5.0.1](https://www.djangoproject.com/)
* [PostgreSQL](https://www.postgresql.org/)
* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)


## Installation

You can easily set up the project by following the steps below. In that case, `Docker` and `Docker Compose` are required.

1. Clone the repo
   ```sh
   git clone https://github.com/joy1954islam/Django-Custom-Authentication-Backend.git
   ```   
2. Run the project.
3. Create a superuser and log in to the Django admin panel.

### Run via manual
Create a virtual environment and install dependency
```sh
cd <project_dir>
virtualenv venv
source venv/bin/activate
pip install requirements.txt
python manage.py runserver
```

### Run via docker
  ```sh
  docker-compose up --build -d
  ```

## Let's Enjoy
```
http://127.0.0.1:8000
```

😊 Happy Coding 😊
