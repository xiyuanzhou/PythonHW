import time


def calculate_time(func):
    def wrapper():
        print (f'Total time {func()}')
        
    return wrapper


@calculate_time
def func():
    return time.time()



