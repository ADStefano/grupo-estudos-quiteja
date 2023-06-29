from worker import celery

# app = Celery('tasks', broker='pyamqp://guest@localhost:5672//')

@celery.task(name='teste')
def teste(x,y):
    soma = x + y
    return soma

