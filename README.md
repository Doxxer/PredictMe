PredictMe
=========

DevDays Fall-2014 project

Requirements
=========
* Python 2.7
* App server
 + Django 1.7 — https://docs.djangoproject.com/en/1.7/intro/install/
 ```
 pip install django
 ```
* Mysql server
 + пароль, имя пользователя, название базы — imdb
 + скачать дамп бд http://dropmefiles.com/cgwYX
 + Создать пользователя imdb с паролем imdb и схему с именем imdb (mysql shell):
 ```sql
create user 'imdb'@'localhost' identified by 'imdb';
create schema 'imdb';
grant all privileges on imdb.* to imdb@localhost;
```
 + импортировать дамп: 
 ```
mysql -u imdb -p -f imdb < /path/to/imdbFULL.sql
```
* IMDBpy library
 + download from http://imdbpy.sourceforge.net/
 + sudo ./setup.py install
* Neural networks
 + MySQLdb (python2 module) — https://pypi.python.org/pypi/MySQL-python/
 + pybrain (python2 module) from http://pybrain.org/docs/ (dependency: SciPy module — http://www.scipy.org/install.html)

How to run
=========
```bash
cd AppServer
./manage.py runserver
```

