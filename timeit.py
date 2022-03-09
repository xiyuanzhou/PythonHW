import time


def calculate_time(func):
    def wrapper():
        begin_time = time.time()
        func()
        finish_run = time.time()
        runtime = finish_run - begin_time
        print(f'Total time {runtime}')
        #return value
        
    return wrapper



@calculate_time
def func():
    time.time()



