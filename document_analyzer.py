



myfile = open('document.txt', 'r')

#print(myfile.read())

words = myfile.read()

#print(words)

count_words = words.split()


cout_word = {}

#for i in range(len(count_words)):
    #count_words[i] = count_words[i].lower() 

for n in count_words:
    if  n not in cout_word.keys():
        cout_word[n] = 1
    else:
        cout_word[n] += 1

mylist = []

for j in cout_word.items():
    mylist.append(j)

for items in range(len(mylist)):
    
    for k in range(0,(len(mylist)- items - 1)):
        if mylist[k][1] < mylist[k+1][1]:
            mylist[k], mylist[k+1] = mylist[k+1], mylist[k]


            
print('')


final_temp = []

for index in range(0,5):
    final_temp.append(mylist[index])

for i in range(len(final_temp)):
    for k in range(0,(len(final_temp)- i - 1)):
        if final_temp[k][0] > final_temp[k+1][0]:
            final_temp[k], final_temp[k+1] = final_temp[k+1], final_temp[k]

for items in range(len(final_temp)):
    
    for k in range(0,(len(final_temp)- items - 1)):
        if final_temp[k][1] < final_temp[k+1][1]:
            final_temp[k], final_temp[k+1] = final_temp[k+1], final_temp[k]

#print(final_temp)

for i in range(len(final_temp)):
    
    print(f'{final_temp[i][0]}: {final_temp[i][1]}')
    
#sort_value = sorted(cout_word.values())


#for key,value in cout_word.items():

#    print(f'{key}: {value}')
    


#print(sort_value)



myfile.close()
    
 
