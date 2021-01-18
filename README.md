# Django-Docker
Django App for local Development 
 To build application run:
 
    docker-compose up -d --build


To run migation use this command:

      docker-compose run web /usr/local/bin/python manage.py migrate

You can see all the swagger endpoint:

      http://127.0.0.1:8000/swagger/

And to reads API docs goto:

      http://127.0.0.1:8000/redoc/
    
