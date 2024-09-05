#count the number of occurrence



# input=[1,2,3,2,1,4,2,5]
#count=2
#output=count of 2 = 3


'''
l=[int(items) for items in input().split(",")]

n=int(input(""))

count=0
for i in l:
    if i==n:
        count+=1
print(count) 
'''

#another approach using inbuilt method 

l=[int(a) for a in input().split(",")]

n=int(input())

count=l.count(n)

print(count)
    