from celery import Celery
from time import sleep

app = Celery('tasks', backend='rpc://', broker='amqp://guest@localhost//')

@app.task
def add(x, y):
    # this in reality would be a much more complicated task
    # add sleep to make it take some time
    sleep(10)
    return x + y
