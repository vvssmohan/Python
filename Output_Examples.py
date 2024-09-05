#example1 
#input="john"
#output="Hello, John!"

'''
name=input("Enter a name: ")
print("Hello",name,sep=", ",end="!")

'''


#example2
#input=5
#output= "you entered:5"

'''
number=int(input("Enter a value:"))
print("You Entered:",number,sep="")

'''

#Example3
#input:3.4 Float input
#output:"value of pi:3.14"

'''

Pi=float(input("Give value of Pi:"))
print("value of Pi:",Pi,sep="")

'''

#example4
#input=10 20 30
#output="sum of input:60"


'''
a=input()
x,y,z=a.split(" ")
sum= int(x)+int(y)+int(z)
print("sum of input:",sum)  

'''

#example5
#input="john",25
#output="Name:john,Age:25"


'''
input=input("Enter Name and Age:")
name,Age=input.split(",")
print("Name:",name,",Age:",Age,sep="")
'''

#Example6
#input=5
#output="countdown:54321 Blast off!"
'''
n=int(input("Enter n:"))
print("Countdown:54321",end="Blast Off!")

'''


#example7
#input=10,5 Arithmetic Operators
#output="addition:15","subtraction:5","mul:50","div:2.0"
'''
x,y=input("Enter a and b values:").split(",")
a=int(x)
b=int(y)
print("Addition:",a+b,",Subtraction:",a-b,",Multiplication:",a*b,",Division:",a/b,sep="")

'''

#example8
#input=10,5  comparision operators
#output="10<5:false,10>5:true,10==5:false,10!=5:true"


'''
x,y=input("Enter A and B values:").split(" ")
a=int(x)
b=int(y)
print("10>5:",a>b,"10<5:",a<b,"10==5:",a==b,"10!=5:",a!=b,sep=(","))

'''


#Example11



x,y=input("Enter name and Age:").split(",")
print(f"Name:{x},Age:{y} years")

