#print n natural numbers
'''
n=int(input("give  n numbers:"))  
i=1
while i<=n:

print(i)
i+=1 #i=i+1    
'''
#print sum of n natural numbers
'''
n= int(input("give n value:"))
i=1
sum=0
while i<=n:
sum +=i
i+=1
print(sum)
'''
#print even numbers
'''
n = int(input("Give N Value:"))
i=1
while i<=n:
if i%2==0:
    print(i)
    i+=1
'''
#print odd numbers
'''
n = int(input("Give N Value:"))
i=1
while i<=n:
if  i%2!=0:
    print(i)
i+=1
'''
#print multiplcation table

'''
n=int(input("give n value:"))
i=1
while i<=10:
    print(f"{n} x {i} = {n*i}")
    i+=1    
       
        #(or)
n=int(input("give n value:"))
for i in range(1,11):
    print(n,"x","=",n*i)
        
'''
#print factoraial

n= int(input("give n value:"))
factorial=1
while n>0:
    factorial=factorial*n
    n=n-1
    print(factorial)   

