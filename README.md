Тестовое задание от ТОО "Somnium"
===============================

Как запустить проект ?
```
docker-compose build
docker-compose up
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
