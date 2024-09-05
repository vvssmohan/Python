'''
Calculator program

input:
num1
num2
operator

output:
perform the operation on the inputs



'''

num1=int(input("Give 1st Number: "))
num2=int(input("Give 2nd Number: "))
operator=input("Give Operator: ")


if operator=="+":
    print(f"Addition of 2 Numbers is:{num1+num2}")
elif operator=="-":
    print(f"Subtraction of 2 numbers is: {num1-num2}")
elif operator=="*":
  print(f"Multiplication of 2 numbers is:{num1*num2}")
elif operator=="/":
    print(f"Division of 2 numbers is:{num1/num2}")
else:
    print("Invalid operator!")
