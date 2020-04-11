FROM python:3.6-alpine
ADD .env.docker /.env
ADD db_check/requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD db_check/db_check.py db_check.py
CMD ["python", "db_check.py"]
# docker build -t db_check -f Dockerfiles/dbcheck/Dockerfile .
