# quartet
metrics box challenge

in this challenge i created the three endpoints called
### /metrics [POST/GET]
### /metrics/aggregate/<timestamp1>/<timestamp2>/<metric_name>
### /metrics/timestamp-metric/<timestamp>/<metric_name>

i decided to use django and the django rest framework because they provided out-of-the-box ease of, from ease of database and model setup including testing of the rest endpoints for verification

## installation & running:
> first created runtime enviroment by installing and using python 2.7 virtualenvwrapper:
```
$ mkvirtualenv -r requirements.pip -p python2.7 poc_env
```

> setup django db
```
$ cd challenge/metricsbox
$ python manage.py migrate
```

> to start the server
```
$ python manage.py runserver
```

> to execute the sample test cases, in another terminal from the same directory
```
$ python manage.py test
```
