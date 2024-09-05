class A:
    __a=10
    ___b=20
    def getPrivateData(self):
        print(self.__a)
        print(self.___b)
        
class B(A):
    def getPrivateMember(self):
        print(self._A__a)  # type: ignore

obj1=A()
print(obj1._A__a) # type: ignore
print(obj1._A___b) # type: ignore

obj2=B()
obj2.getPrivateMember()
print(obj2._A__a)# type: ignore

