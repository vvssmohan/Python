#method oerloading in import the module.
'''
import multipledispatch
class A:
    @multipledispatch.dispatch(int,int)
    def add(self,a,b):
        return a+b
    @multipledispatch.dispatch(int,int,int)
    def add(self,a,b,c):
        return a+b+c
    @multipledispatch.dispatch(str,str)
    def add(self,a,b):
        return a+b
    
obj=A()
print(obj.add(1,2,3))
print(obj.add(1,2))
print(obj.add('mohan','ramanam'))

'''
# methodoverloading in simple way


class A:
    def add(self,*args):
     if args:
        sum=type(args[0])()
        for i in args:
            sum=sum+i
        return sum
    
obj=A()

print(obj.add(1,2))
print(obj.add(1,2,3))
print(obj.add(1,2,3,4))
print(obj.add('a','b','c'))
print(obj.add(12.3,3.4,5.6))
print(obj.add([1,2],[3,4]))
print(obj.add(1,2,3,4.5,2.6))


