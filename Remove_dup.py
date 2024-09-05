#remove duplicate elements 
#hard approach
'''
l=[int(item) for item in input().split(",")]

NewL=[]

for i in l:
    if i in NewL:
        continue
    else:
        NewL.append(i)
print(NewL)
'''

#easy approach

inp =input().split(",")

l=[int(a) for a in inp]

s=set(l)

newl=list(s)

print(newl)
