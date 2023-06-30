# Простое todo приложение для повседневной жизни

## Запуск через docker

Скачиваем с докер хаба и запускаем контейнер

`docker run -d -p 8000:8000 --rm --name todo_app sumrock/todo_app_django`

## Запуск в своем окружении

переходим в папку с проектом `cd todo_app_django`

создаем окружение(если необходимо) `python -m venv venv`

активируем его `. venv/bin/activate`

усанавливаем зависимости `pip install -r requirements.txt`

проводим миграции `python manage.py migrate`

запускаем сервер `python manage.py runserver`