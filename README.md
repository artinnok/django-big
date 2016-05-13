# Default Django Skeleton

Python Interpreter version: 3.4.3+

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
```
git clone git@github.com:artinnok/django-default-skeleton.git
django-default-skeleton_project
```

### Create virtual environment
On repository level
```
virtualenv env -p python3
```

### Activate virtual environment
On repository level
```
source env/bin/activate
```

### Install requirements
On project level
```
pip install -r requirements/local.txt
```


