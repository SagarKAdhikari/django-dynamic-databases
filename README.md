# django-dynamic-databases
A django demo project to show routing in dynamically created databases. 

<b> CREDIT</b> : This project is in line with the stack overflow answer by <b>iancoleman</b> on https://stackoverflow.com/questions/6585373/django-multiple-and-dynamic-databases

In this demo, a database is created for each user. We identify the user from request and do actions on the corresponding user database.

1. When a new django user is created, a database with unique name <b>b+'username'</b>, is created. 
2. A middleware is written, which identifies the request user and routes to the user specific database accordingly. For the requests that come from users who are not logged in, we simple route to the default database, named 'default' in settings.py.
