import time


def calculate_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'Total time: {str(end - start)}')
        
        
    return wrapper

@calculate_time
def func():
    return time.time()



