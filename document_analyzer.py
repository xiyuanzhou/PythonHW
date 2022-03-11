



myfile = open('document.txt', 'r') #open the file 

#print(myfile.read())


words = myfile.read() # read the files into string variable

#print(words)

#split the sentence into single words
count_words = words.split()


cout_word = {}

#stored all the words in to dictionary
#also count the same words and save into dictionary
for n in count_words:
    
    if  n not in cout_word.keys(): #if not the same word
        cout_word[n] = 1
    else:
        cout_word[n] += 1

mylist = []

#move all the dictionary keys and values into a list
for j in cout_word.items():
    mylist.append(j)

#sort the list base on values 
for items in range(len(mylist)):
    
    for k in range(0,(len(mylist)- items - 1)):
        #bigger to smaller
        if mylist[k][1] < mylist[k+1][1]: 
            mylist[k], mylist[k+1] = mylist[k+1], mylist[k]


            
print(' ')


final_temp = []

#after sort, take top five 
#appened into a new list
for index in range(0,5):
    final_temp.append(mylist[index])

    
#sort the new list base on alpha
for i in range(len(final_temp)):
    for k in range(0,(len(final_temp)- i - 1)):
        if final_temp[k][0] > final_temp[k+1][0]:
            final_temp[k], final_temp[k+1] = final_temp[k+1], final_temp[k]


#sort the new list base on values again
for items in range(len(final_temp)):
    
    for k in range(0,(len(final_temp)- items - 1)):
        if final_temp[k][1] < final_temp[k+1][1]:
            final_temp[k], final_temp[k+1] = final_temp[k+1], final_temp[k]

#print(final_temp)

#now this is the final answer
#print all five item from the list 
for i in range(len(final_temp)):
    
    print(f'{final_temp[i][0]}: {final_temp[i][1]}')
    
#sort_value = sorted(cout_word.values())


#for key,value in cout_word.items():

#    print(f'{key}: {value}')
    


#print(sort_value)



myfile.close()
  
#code by Xiyuan Zhou
 
