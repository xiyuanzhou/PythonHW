def doubler(func):
    
    def wrapper():
        
        func()
        func()
        
    return wrapper


@doubler
def func():
    print('test')
    
