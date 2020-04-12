create a new django project

```bash
$ django-admin startproject mysite
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
