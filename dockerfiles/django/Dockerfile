FROM python:3.6-slim
RUN apt-get update && apt-get install postgresql-client -y
ENV working_directory=/app
RUN mkdir -p $working_directory
WORKDIR $working_directory
# add the application root folder to the contaner
# depends on where this Dockerfile is stored
ADD . $working_directory
RUN chmod +x wait-for-postgres.sh
RUN pip install -r requirements.txt
ADD .env.docker  $working_directory/.env
#CMD ["ls", "-la"]
#CMD ["pwd"]
CMD ["./wait-for-postgres.sh","db","python","manage.py","runserver","0.0.0.0:8000"]
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# docker build -f dockerfiles/django/Dockerfile -t django-api:alpine .
# docker run django-api:alpine -p 8000:8000
