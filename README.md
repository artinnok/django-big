# Django Default

## Intro

### This cookiecutter main features
* Settings splitted into **base/local/production**
* Requirements splitted into **base/local/production**
* Urls splitted into **base/local/production**
* Fabfile for remote deployment
* Celery for asynchronous tasks
* Common behaviors (mixins) for models
* Common models
* webpack.js for static files handling

### Python Interpreter version
* Python 3.4.3+

### Main project dependencies
* [Django](https://www.djangoproject.com/) - Python MVC web framework
* [Celery](http://www.celeryproject.org/) - asynchronous queue
* [Fabric](http://www.fabfile.org/index.html) - deployment and system
administration tool
* [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/#) - command
line tool that creates projects from
templates
* [webpack.js](http://webpack.github.io/) - module bundler
* [npm.js](https://www.npmjs.com/) - package manager for javascript

### OS requirements
* Mac OS X
* UNIX like OS



## Work with cookiecutter

### Clone project
```bash
git clone git@github.com:artinnok/django-default.git
```

### Install cookiecutter
```bash
[sudo] pip install cookiecutter
or
[sudo] easy_install cookiecutter
or on Mac OS X
[sudo] brew install cookiecutter
```

### Start interactive cookiecutter install process:
```bash
cookiecutter django-default
```
After fast installation proccess you receive **yoursite_project** with
structure:

*Repository level*:
```
yoursite_project/
├── README.md
├── django-default
└── env
```

*Project level*:
```
yoursite/
├── config
├── core
├── manage.py
├── requirements
└── templates
```

*App level*:
```
core/
├── __init__.py
├── admin.py
├── apps.py
├── behaviors.py
├── common_models.py
├── migrations
├── models.py
└── views.py
```

### Install virtualenv
```bash
[sudo] pip install virtualenv
or
[sudo] easy_install virtualenv
or on Ubuntu
[sudo] apt-get install virtualenv
```

### Create virtual environment for **yoursite_project**
```bash
cd yoursite_project # repository level
virtualenv -p python3 env
```

### Generate your project SECRET_KEY
You can generate key via django-extensions:
```bash
python manage.py generate_secret_key
```

Or at [this site](http://www.miniwebtool.com/django-secret-key-generator/).

### Add your SECRET_KEY
Open in your preferred text editor (vim, nano etc.) file *env/bin/activate*
and prepend to end this part:
```bash
export SECRET_KEY='here your generated key'
export DJANGO_SETTINGS_MODULE='config.settings.local'
```

### Activate virtual environment
```bash
source env/bin/activate
```

### Install requirements
```bash
cd yoursite # project level
pip install -r requirements/local.txt
```

### Run local server
On project level:
```bash
python manage.py runserver --settings config.settings.local
```
### Enjoy!
