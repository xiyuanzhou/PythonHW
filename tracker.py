def func_counter(func):
    
    def wrapper():
        
        func()
        
        
    
    return wrapper


@func_counter
def func():
    print("uuuu")
    
    
func()
