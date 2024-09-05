'''
def add_numbers (a,b):
return a+b 
result=add_numbers(5,3)
print(result)      #Function-positional argument

'''

#keyword arguments
'''
def personal_info(name,age):

    print("name:",name)
    print("age",age)
    personal_info(age=21,name="mohan")
    
    
   ex-2
    
def my_function(Name, Age):
  print("WELCOME! " + Name,Age)

my_function(Name="MOHAN",Age=21)
    
'''


#Default arguments

def greet_user(name,greeting="hello"):
    return greeting+", "+name+"!"
greeting1=greet_user("Bob")
greeting2=greet_user("charlie","hi")
print(greeting1)
print(greeting2)