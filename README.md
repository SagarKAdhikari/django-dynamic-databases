# django-dynamic-databases
A django demo project to show routing in dynamically created databases.

1. When a new django user is created, a database with unique name <b>b+'username'</b>, is created. 
2. A middleware is written, which identifies the request user and routes to the user specific database accordingly.
