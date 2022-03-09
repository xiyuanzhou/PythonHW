import time


def calculate_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        runtime = end - start
        print(f'Total time {runtime}')
        #return value
        
    return wrapper



@calculate_time
def func():
    time.time()



