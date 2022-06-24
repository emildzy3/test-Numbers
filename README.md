# Тестовое задание для компании Numbers

## О проекте
___
В результате выполнения проекта разработан скрипт для синхронизации данных из [Google Sheets](https://docs.google.com/spreadsheets/d/1VuNKORnuTib8k1mMIjqrEms6VungKDuveLvJFMCza4c/edit#gid=0) с БД Postgresql. Также в рамках выполнения Т.З. написан Telegram bot для уведомления пользователей об нарушении срока поставки товара и создан одностраничный веб-сайт. 

[тестовое здание](https://github.com/emildzy3/test-Numbers/blob/main/%D0%A2%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20(developer).pdf)

## Запуск и установка проекта 
___

1. Добавьте проект в рабочую директорию

```
git clone https://github.com/emildzy3/test-Numbers.git
```
2. Получите Token у телеграм-бота @BotFather
3. Добавить его в файл tg_bot/config.py
```
token = '........'
```
### С помощью Docker
3. Cоздать контейнеры docker
```
docker-compose build
```
5. Запустить приложение
```
docker-compose up
```
6. Применить миграции
```
docker exec -i $(docker ps | grep server_ | awk '{{ print $1 }}') python manage.py migrate
```
### Без Docker

3. Создайте и активируйте виртуальное окружение

```
python3.10 -m venv venv && source venv/bin/activate
```

4. Установите необходимые пакеты. Файлы requirements.txt находятся в каждой папке проекта
```
pip install -r requirements.txt
```
5. Создайте пользователя для Postgresql:
```
sudo -u postgres psql
CREATE DATABASE number;
CREATE USER user WITH PASSWORD '111';
ALTER ROLE user SET client_encoding TO 'utf8';
ALTER ROLE user SET default_transaction_isolation TO 'read committed';
ALTER ROLE user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE number TO user;
ALTER DATABASE number OWNER TO user;
```
6. В настройках приложений (в каждой папке - settings.py) замените параметры БД
```
DATABASE = "..."
USER = "..."
PASSWORD = "...."
HOST = "localhost"
PORT = "5432"
```

7. Производите миграции 
```
python manage.py migrate 
```
5. Запустите каждое приложение по отдельности
```
python3 server.py
python3 update_data_Gsheets.py
python3 manage.py runserver
```
