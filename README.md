https://github.com/jaabberwocky/dataeng_test

### q1: data pipeline

### q2: postgres db

```bash
docker image build -t postgres_db . --no-cache
docker container run -d --name postgres_db postgres_db
docker container exec -it postgres_db psql -U admin test_db

# to show table schema
test_db-# \d car
 
```

https://dbdiagram.io/d/5f74b9073a78976d7b75ded8

### q3: architecture design

