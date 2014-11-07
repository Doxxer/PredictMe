PredictMe
=========

DevDays Fall-2014 project

Requirements
=========

* Mysql server
 + пароль, имя пользователя, название базы -  imdb2 
 + соответственно mysql -u imdb2 -p -f imdb2 < /path/to/new.sql
* IMDBpy library
 + download from http://imdbpy.sourceforge.net/
 + sudo ./setup.py install
* Neural networks
 + MySQLdb (python2 module) — https://pypi.python.org/pypi/MySQL-python/
 + pybrain (python2 module) from http://pybrain.org/docs/ (dependency: SciPy module — http://www.scipy.org/install.html)
* App server
 + Django - https://docs.djangoproject.com/en/1.7/intro/install/
 + скачать дамп бд http://dropmefiles.com/cgwYX

How to run
=========
```bash
cd AppServer
./manage.py runserver
```

