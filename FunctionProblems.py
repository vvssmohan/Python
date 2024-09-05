#sum of two numbers using function call
'''

a= int(input("Give a value:"))
b= int(input("Give b value:"))

def add2numbers(a,b):
    print(a+b)
add2numbers(a,b)


#Area of circle


def area (r):
    input("enter radius:")
    circlearea = 3.14*(r**2)
    return circlearea
radius=20
a=area(radius)
print(a)



'''

#swap of a values

def swap(a,b):
        b=b+a
        a=b-a 
        b=b-a
        print(f"value of a is:{a}")
        print(f"value of b is:{b}")

swap(5,10)