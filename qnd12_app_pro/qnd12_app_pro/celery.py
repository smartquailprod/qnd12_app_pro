import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qnd12_app_pro.settings.pro')

app = Celery('qnd12_app_pro')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
