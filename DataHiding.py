class Bank:
 __balance=1000
def getbalance(self):
        return self.__balance
        
class API(Bank):
    def printbalance(self):
        return self.__balance
    
    
# Here we have accessed the private data
# member through class name.
obj1=Bank()
print(obj1._Bank__balance)  # type: ignore

obj2=API()
print(obj2._Bank__balance) # type: ignore