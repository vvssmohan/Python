#how to create a object.
'''
class my_name:
    fullname="RAMANAM MOHAN"
obj1=my_name()
print(obj1.fullname)

'''
#update the attribute value 
  #obj1 have changed but other object doesen't change.

'''
class Sampleclass:
    Attribute1=10
    Attribute2=20
obj1=Sampleclass()
obj2=Sampleclass()
obj3=Sampleclass()

obj1.Attribute2=100

print(obj1.Attribute2)
print(obj2.Attribute2)
print(obj3.Attribute2)
    
''' 
#all the object access with the class.
#attribute value are changed.


class Sampleclass:
    Attribute1=10
    Attribute2=20
obj1=Sampleclass()
obj2=Sampleclass()
obj3=Sampleclass()

Sampleclass.Attribute1=1000

print(obj1.Attribute1)
print(obj2.Attribute1)
print(obj3.Attribute1)