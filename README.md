# luchanos_oxford_university

To make migrations, if you don't have alembic.ini yet, you need to execute the next command in terminal:

```
alembic init migrations
```

After that will be created a folder with migrations and configuration file for alembic.

- In alembic.ini you need to determine database address where you want to make migrations.
- Then we go to the folder with migrations and open env.py, there we make changes in the block that contains 

```
from myapp import mymodel
```

- Then execute: ```alembic revision --autogenerate -m "comment"```
- After that will be made a migration
- Then enter: ```alembic upgrade heads```
