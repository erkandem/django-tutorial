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
