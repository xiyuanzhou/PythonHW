import time


def calculate_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        runtime = end - start
        print(f'Total time: {str(runtime)}')
            
    return wrapper


@calculate_time
def func():
    return time.time()

