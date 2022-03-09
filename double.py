def doubler(func):
    
    def wrapper():
        
        func()
        
        
    return wrapper


@doubler
def func():
    print('test')
    
