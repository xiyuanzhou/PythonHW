import time


def calculate_time(func):
    def wrapper():
        
        start = time.time()
        end = time.time()
        
        print (f'Total time: {func(end - start)}')
    return wrapper

@calculate_time
def func(times):
    return times



