'''
l=[10,20,30,40,50]

sum=0
for i in l:
    sum+=i
print(sum)

'''
        #(or)
        
'''       
l=[10,20,30,40,50]
length=len(l)
sum=0
for i in range(length):
    sum=sum+l[i]
print(sum)
'''
        #using while loop
'''   
l=[10,20,30,40,50]
sum=0
i=0
length=len(l)
while i<length:
    sum=sum+l[i]
    i+=1
print(sum)
'''

#find the max and min
'''
l=[10,20,30,50,7,77,777]

max=l[0]
min=l[0]
for i in l:
    if i>max:
        max=i
    if i<min:
        min=i
print(max,min)
'''
    #using short method
    
    
l=[10,27,77,20,30,50,7,18]

l.sort()
#print(l)
print(l[0],l[-1])
