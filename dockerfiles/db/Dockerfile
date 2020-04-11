FROM postgres:12-alpine
ENV POSTGRES_PASSWORD=postgres
COPY init.sql /docker-entrypoint-initdb.d/

# docker build -f dockerfiles/db/Dockerfile -t django_database:12-alpine .
# docker run -p 5433:5432 django_database:12-alpine