from worker import config
from celery import Celery

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

class Config:

    CELERY_RESULT_BACKEND = config.CELERY_RESULT_BACKEND
    CELERY_BROKER_URL = config.CELERY_BROKER_URL
    CELERY_ROUTES = {'teste': {'queue': 'teste'}}
    # task_queue = ('Queue'(name = 'teste'))



celery = Celery()
celery.config_from_object(Config)

# docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.12-management