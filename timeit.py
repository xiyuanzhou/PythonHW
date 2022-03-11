import time


def calculate_time(func):
    def wrapper():
        
        #initial starting time 
        begin_time = time.time()
        func()
        
        #time end here 
        finish_run = time.time()
        
        #final running time for the function called
        runtime = finish_run - begin_time
        
        #print result
        print(f'Total time {runtime}')
        #return value
        
    return wrapper



@calculate_time
def func():
    time.time()

#code by Xiyuan Zhou

