#for loop
'''
candies=10
for i in range(candies):
    print("given to friend")
print(candies)

'''


#while loop

'''
candies=10
while candies>0:
    print("give to friend")
    candies-=1
print(candies)

'''
#Nested loop

#print 1 to 5 tables 

'''
for i in range (1,6):
    for j in range(1,11):
        print(f" {i} * {j} = {i*j}")
        
'''


#break 
'''
candies=10
for i in range (candies):
    print("giving a candies to a friend")
    if candies-i==6:
        print("only 5 candies left.stop it")
        break
'''


#continue


candies=10
for i in range (candies):
    if candies-i==5:
        print("this is a special chocolate.skip this one")
        continue
    print("giving a candies to a friend")
