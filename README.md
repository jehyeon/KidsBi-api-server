# KidsBi server

### How to migrate model
```
$ python manage.py makemigrations <model>
$ python manage.py migrate <model>
```

### How to local test
on Window
```
$ heroku local web -f Procfile.windows
```
on Mac
```
$ heroku local web
```
