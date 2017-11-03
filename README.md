# quartet
metrics box challenge

in this challenge i created the three endpoints called
```
/metrics [POST/GET]
```
```
/metrics/aggregate/<timestamp1>/<timestamp2>/<metric_name> [GET]
```
```
/metrics/timestamp-metric/<timestamp>/<metric_name> [GET]
```

i decided to use django and the django rest framework because they provided out-of-the-box ease of database and model setup, including testing of the rest endpoints for verification

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

> to execute the sample test cases
```
$ python manage.py test
```

> to manually run sample queries against the rest api, use curl
```
curl -H "Content-Type: application/json" -X POST "http://localhost:8000/metrics" -d "{\"timestamp\":5,\"name\":\"response_time\",\"value\":1}"
```
```
curl -H "Content-Type: application/json" -X GET "http://localhost:8000/metrics"
```
```
curl -H "Content-Type: application/json" -X GET "http://localhost:8000/metrics/timestamp-metric/5/response_time"
```
```
curl -H "Content-Type: application/json" -X GET "http://localhost:8000/metrics/aggregate/4/6/response_time"
```
