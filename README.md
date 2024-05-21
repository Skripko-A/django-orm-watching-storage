# Пишем пульт охраны банка
Django проект, веб сайт службы безопасности банка, выполнябщий функции мониторинга карт доступа и анализа посещений хранилища.


### Как установить
Python3 должен быть установлен.  
Скачайте проект.  
Создайте виртуальное окружение и установите зависимости:

```commandline
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```


### Запуск
```commandline
python3 main.py
```
Перейдите по ссылке http://0.0.0.0:8000  


### Демонстрация работы сайта
Страница активных карт доступа:
![](https://github.com/Skripko-A/django-orm-watching-storage/blob/master/active_passcards_page.png)  
Страница списка людей в хранилище:
![](https://github.com/Skripko-A/django-orm-watching-storage/blob/master/storage_info_view.png)  
Станица списка посещений хранилища по конкретному ключу:  
![](https://github.com/Skripko-A/django-orm-watching-storage/blob/master/passcard_info_view.png)

### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).