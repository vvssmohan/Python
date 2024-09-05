a = input("Give a numbers:")

x,y,z =a.split(",")

num1 =int(x)
num2 =int(y)
num3 =int(z)
gratest =0
if num1>num2:
    if num1>num3:
        gratest=num1
    else:
        gratest=num3
elif num2>num1:
    if num2>num3:
        gratest = num2
    else:
        gratest=num3  
elif num3>num1:
    if num3>num2:
        gratest =num3
    else:
        gratest=num2
print(gratest)      
