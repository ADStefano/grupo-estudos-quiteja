from celery import signature

def signature(name, **args,**kwargs):

    if not args:
        

signature('teste', args=(23,2))