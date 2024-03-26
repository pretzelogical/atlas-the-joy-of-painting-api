FROM mysql:8.3.0

ENV MYSQL_ROOT_PASSWORD=pass
EXPOSE 3306
COPY ./init.sql /docker-entrypoint-initdb.d
