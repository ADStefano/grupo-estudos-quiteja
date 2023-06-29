def teste_task(x,y):
    from worker.tasks import teste
    teste.delay(x, y)

if __name__ == '__main__':
    teste_task(22,3)