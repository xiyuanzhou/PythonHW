def sort_list(mylist):
    
    #get the size/length of mylist list 
    n = len(mylist)
    i = 0
    
    #start the first loop for the whole 
    while i < n - 1:
        k = 0
        
        #checking the rest loop index
        #excpet for the iter index
        while n - i - 1 > k:
            
            #compare the value
            #if bigger then swap
            if mylist[k] > mylist[k + 1]:
                mylist[k], mylist[k + 1] = mylist[k + 1], mylist[k]
            
            k = k + 1
                
        i = i + 1 
        
    return mylist


#code by Xiyuan Zhou
