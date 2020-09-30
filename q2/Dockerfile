FROM postgres:latest
COPY create_table.sql /docker-entrypoint-initdb.d/create_table.sql
ENV POSTGRES_USER admin
ENV POSTGRES_PASSWORD admin
ENV POSTGRES_DB test_db
