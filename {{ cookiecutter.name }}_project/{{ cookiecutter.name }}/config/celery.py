from __future__ import absolute_import, unicode_literals

from celery import Celery

app = Celery('celery')

app.config_from_object('config.settings.celery', namespace='CELERY')
app.autodiscover_tasks()
