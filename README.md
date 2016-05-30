# Default Django Skeleton

### Intro
This is my preferred Django Skeleton. I hope this was built at the top of best
practices and approaches.

Pull requests are welcome!

### This skeleton main features
* Settings splitted into *base/local/production/packages*
* Requirements splitted into *base/local/production*
* Urls splitted into *base/local/production*
* Celery added

### Python Interpreter version
* Python 3.4.3+

### Main project dependencies
* [Django](https://www.djangoproject.com/) - MVC web framework
* [RabbitMQ](http://www.rabbitmq.com/) - broker for Celery
* [Celery](http://www.celeryproject.org/) - asynchronous queue

### OS requirements
* Mac OS X
* UNIX like OS

### Project structure
Repository level:
```
django-default-skeleton_project/
├── README.md
├── django-default-skeleton
└── env
```

Project level:
```
django-default-skeleton/
├── config
├── core
├── manage.py
├── requirements
└── templates
```

App level:
```
core/
├── __init__.py
├── admin.py
├── apps.py
├── forms.py
├── migrations
├── models.py
├── tasks.py
├── tests.py
└── views.py
```
## Work with skeleton

### Clone project
```bash
git clone git@github.com:artinnok/django-default-skeleton.git django-default-skeleton_project
```

### Create virtual environment
On repository level:
```bash
virtualenv -p python3 env 
```

### Activate virtual environment
On repository level:
```bash
source env/bin/activate
```

### Install requirements
On project level:
```bash
pip install -r requirements/local.txt
```

### Generate your project SECRET_KEY
You can generate key via django-extensions:
```bash
python manage.py generate_secret_key
```

Or at [this site](http://www.miniwebtool.com/django-secret-key-generator/).

### Add your SECRET_KEY
Open in your preferred text editor (vim, nano etc.) file *env/bin/activate*
and
prepend to
end this part:
```bash
export SECRET_KEY='here your generated key'
```

### Rectivate virtual environment
On repository level:
```bash
source env/bin/activate
```

### Install RabbitMQ
Tutorial [here](http://www.rabbitmq.com/install-debian.html).

### Run local server
On project level:
```bash
python manage.py runserver --settings config.settings.local
```
### Enjoy!
