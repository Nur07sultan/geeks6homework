import os

from celery import Celery
from celery.beat import crontab
from celery.schedules import crontab

print(">>> users.tasks imported")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

app = Celery('main', include=['users.tasks'])

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    "send_daily_report": {
        "task": "users.tasks.send_daily_report",
        "schedule": crontab(minute="*")
    }
}
