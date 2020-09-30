https://github.com/jaabberwocky/dataeng_test

### q1: data pipeline

to setup crontab: 

```bash
crontab -e
```

```bash
* * * * * /usr/bin/python /path/to/process.py >> $HOME/`date +\%Y\%m\%d\%H\%M\%S`-cron.log 2>&1
```

edit crontab as above and the script will run on 1am every day with output log file yyyyMMddHHMMSS-cron.log generated


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

