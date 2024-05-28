# Пишем пульт охраны банка
Django проект, веб сайт службы безопасности банка, выполнябщий функции мониторинга карт доступа и анализа посещений хранилища.


### Как установить
Python3 должен быть установлен.  
Скачайте проект.  
Создайте виртуальное окружение и установите зависимости:

```commandline
python3 -m venv env
```
```commandline
source env/bin/activate
```
```commandline
pip3 install -r requirements.txt
```
Создайте файл для хранения переменных окружения:
```commandline
touch .env.private_settings
```
Структура вашего файла .env.private_settings:
```
ALLOWED_HOSTS = 'разрешенные хосты'
SECRET_KEY = 'ваш secret_key'
DEBUG = True или False

DB_URL = 'postgres://db_user:password@db_host:port/db_name'
```
В кавычкх ('') необходимо указать соответствующие настройки БД.
### Запуск
```commandline
python3 manage.py runserver localhost:8000
```
Перейдите по ссылке http://localhost:8000


### Демонстрация работы сайта
![](https://github.com/Skripko-A/django-orm-watching-storage/blob/master/django-orm-watching-storage-demo.gif)
### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).