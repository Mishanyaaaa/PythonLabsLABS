# LAB3
1. Виконав команди для встановлення бібліотек та запуску серверу:
    * `pipenv install django`
    * `pipenv run django-admin startproject my_site`
    * `mv my_site/my_site/* my_site/` 
    * `mv my_site/manage.py ./`
    * `pipenv run python manage.py runserver` 
2. створив шаблон: 
    * `pipenv run python manage.py startapp main`
3. Встановив бібліотеку: 
    * `pipenv install requests`
4. Дописав функцію health()
5. Дописав перевірку для роботи сервера
6. В monitoring.py зробив виклик функції кожної хвилини за допомогою циклу while та бібліотеки time
7. Написав аліас
