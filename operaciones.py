from celery import Celery
app = Celery('operaciones',broker = 'redis://localhost:5050', backend = 'redis://localhost:5050', include =['cliente_celery', 'server_celery'])

@app.task
def resta(x, y):
    return x-y

@app.task
def suma(x, y):
    return x+y

@app.task
def mult(x, y):
    return x*y

@app.task
def power(x, y):
    return x**y

@app.task
def division(x, y):
    if y==0:
        return 'Error, denominador=0'
    else:
        return x/y

