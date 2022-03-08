def sort_list(mylist):
    n = len(mylist)
    i = 0
    while i < n - 1:
        k = 0
        while n - i - 1 > k:
            
            if mylist[k] > mylist[k + 1]:
                mylist[k], mylist[k + 1] = mylist[k + 1], mylist[k]
            
            k = k + 1
                
        i = i + 1
        
    return mylist
