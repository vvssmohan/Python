'''
a =int(input("Give a:"))
b =int(input("Give b:"))

temp=b
b=a
a=temp

print(f"value of a is:{a}")
print(f"value of b is:{b}")
'''
#without using temp variable

a= int(input("Give a :"))
b= int(input("Give b :"))

b= b+a
a=b-a
b=b-a
print(f"values of a is:{a}")
print(f"values of b is:{b}")