PredictMe
=========

DevDays Fall-2014 project

Requirements
=========

* Mysql server
 + пароль, имя пользователя, название базы -  imdb2 
* IMDBpy library
 + download from http://imdbpy.sourceforge.net/
 + sudo ./setup.py install
* Neural networks
 + MySQLdb (python2 module) — https://pypi.python.org/pypi/MySQL-python/
 + pybrain (python2 module) from http://pybrain.org/docs/ (dependency: SciPy module — http://www.scipy.org/install.html)
* App server
 + Django - https://docs.djangoproject.com/en/1.7/intro/install/
 + скачать дамп бд http://dropmefiles.com/cgwYX
 + выполнить mysql -u imdbFULL -p -f imdbFULL < /path/to/new.sql

How to run
=========
```bash
cd AppServer
./manage.py runserver
```

