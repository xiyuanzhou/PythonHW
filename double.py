def doubler(func):
    
    def wrapper():
        
        #call two function 
        func()
        func()
        
    return wrapper


@doubler
def func():
    print('test')
    
#code by Xiyuan Zhou
    
