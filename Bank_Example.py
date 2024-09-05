class BankingAccount:
    def __init__(self,AccountNo,AccountName,IFSC_code,Balance):        
     self.AccountNo=AccountNo
     self.AccountName=AccountName
     self.IFSC_code=IFSC_code
     self.Balance=Balance
    def withdraw(self,amount):
        self.Balance=self.Balance-amount
    def deposit(self,amount):
        self.Balance+=amount
    def checkBalance(self):
        print(self.Balance)
        #print(" AccountNo:{}\n AccountName:{}\n IFSC_code:{}\n Balance:{}\n".format(self.AccountNo,self.AccountName,self.IFSC_code,self.Balance))
Account1=BankingAccount(12344559,'MOHAN','VDL0987',7000)
Account2=BankingAccount(12345,'DHONI','VDL0007',7777)
print(Account1.AccountName)
print(Account2.AccountName)
#Account1.checkBalance()
#Account1.deposit(3000)
#Account1.checkBalance()
#Account1.withdraw(5000)
#Account1.checkBalance()