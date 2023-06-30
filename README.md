# Простое todo приложение для повседневной жизни

## Запуск через docker

Скачиваем с докер хаба и запускаем контейнер

`docker run -d -p 8000:8000 --rm --name todo_app sumrock/todo_app_django`

## Запуск в своем окружении

создаем окружение(если необходимо) `python -m venv venv`

проводим миграции `python manage.py migrate`

запускаем сервер `python manage.py runserver`