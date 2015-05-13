# encoding:utf-8
from django.conf import settings

from celery import Celery


CELERY_BACKEND = getattr(settings, 'CELERY_BACKEND', 'amqp://')

CELERY_RABBITMQ_REPORT = getattr(settings, 'CELERY_RABBITMQ_REPORT')

REPORT_TASK_NAME = getattr(settings,
                           'REPORT_TASK_NAME', 'reports.tasks.save_report')


_app = None


def _get_celery_app():
    global _app
    if not _app:
        _app = Celery(
            CELERY_RABBITMQ_REPORT[0],
            broker=CELERY_RABBITMQ_REPORT[1],
            backend=CELERY_BACKEND,
        )
    return _app


def send_report(report):
    _get_celery_app().send_task(REPORT_TASK_NAME, [report])
