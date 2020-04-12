create a new django project

```bash
$ django-admin startproject <project_name>
```

create a new django app

```bash
$ django-admin startapp <app_name>
```

apply all database operations on a new database

```bash
$ python manage.py migrate
```

after adding or changing an existing model the database need to be adjusted
for potential schema changes, data type changes etc.

stored within the `migrations` package in the individual app

```bash
$ python manage.py makemigrations <app_name>
```


the raw SQL version may be checked out with the `sqlmigrate` command

```bash
$ python manage.py sqlmigrate my_app 0001 > sql.sql
```

drop a shell in the container. typically the database
```bash
$ docker container ls
$ docker exec -it 2d02552125ab '/bin/sh'
```

start the database
```bash
docker run -p 5433:5432 -v django_database:/var/lib/postgresql/data django_database:12-alpine
```
stop the database gracefully:
```bash
docker container stop <container ID>
```
2c92ffc17594df172f03180881ebec154cc35d0883f3640db5e80ddba67f341f

___
 
search for a specific command which might be in the code base 

```bash
$ grep -r exec . --exclude-dir venv --exclude-dir .idea --exclude-dir .git
```

---
pip caching strategy

will download packages and dependencies
into a local folder
Add them to `.dockerignore`

```bash
$ mkdir pip_cache \
  && cd pip_cache \
  && pip download -r ../requirements.txt
```
**aborted since file system cache can't be used from inside a docker container during built time.
The packages would need to be made available via networking (static file host)**


___
# tests
be sure to grant the right to create, act on created and delete databases to the django application
on the database server

```sql
ALTER ROLE django_app WITH SUPERUSER;
```

run the tests

```bash
python manage.py test my_app
```

or with coverage
```bash
coverage run --source='.' --omit='./venv/*' manage.py test my_app
coverage html
firefox htmlcov/index.html
```
