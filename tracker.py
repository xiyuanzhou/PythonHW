def func_counter(func):
    def wrapper():
        
        #keep track on how many time being call
        #add one each time
        wrapper.counter += 1
        return func
    wrapper.counter = 0
    
    return wrapper


@func_counter
def foo():
    return 2**3-34

#code by Xiyuan
#foo()
#foo()
#print(foo.counter) # expect 2 as output
    
    
