# from __future__ import absolute_import
# import os
# from celery import Celery
# from django.conf import settings
#
#
# # set the default Django settings module for the 'develop' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'develop.settings')
#
# app = Celery('develop')
#
# # Using a string here means the worker will not have to
# # pickle the object when using Windows.
# app.config_from_object('django.conf:settings')
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
#
#
# @app.task(bind=True)
# def debug_task(self):
#     return print('Request: {0!r}'.format(self.request))
#
# """
# TUTS:
#  - ref: http://celery.readthedocs.org/en/latest/django/first-steps-with-django.html#using-celery-with-django
#  `` (newsroom) newsroom_django@beta:$ celery -A newsroom worker -l info ``
#  `` (newsroom) newsroom_django@beta:$ celery help ``
#  `` (newsroom) newsroom_django@beta:$ celery -A newsroom beat  ``
#  `` (newsroom) newsroom_django@beta:$ celery -A newsroom worker -B -l info   ``
#  `` (newsroom) newsroom_django@beta:$ celery -A newsroom worker --loglevel=DEBUG --beat   ``
#  `` (newsroom) newsroom_django@beta:$ celery multi start -A newsroom w1 --beat -l info   `` *
#  `` (newsroom) newsroom_django@beta:$ celery multi start -A newsroom w1 --beat -l info --statedb=/webapps/newsroom/run/celery/%n.state  ``
#
#
#
#  `` (newsroom) newsroom_django@beta:$ celery -A app worker -l info
#  `` (newsroom) newsroom_django@beta:$ celery beat -A app ``
#
#
#  - this one worked:
#    https://www.digitalocean.com/community/tutorials/how-to-use-celery-with-rabbitmq-to-queue-tasks-on-an-ubuntu-vps
#
#    celery -A newsroom worker -B -l info &
# """
#
# app.conf.update(
#     BROKER_URL='redis://localhost:6379/0',
#     CELERYBEAT_SCHEDULER='djcelery.schedulers.DatabaseScheduler',
#     CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend',
#     CELERY_DISABLE_RATE_LIMITS=True,
#     CELERY_ACCEPT_CONTENT=['json', ],
#     CELERY_TASK_SERIALIZER='json',
#     CELERY_RESULT_SERIALIZER='json',
# )
