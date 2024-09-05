#CREATE A CLASS OF BANKACCOUNT

'''
class BankingAccount:
    def __init__(self,AccountNo,AccountName,IFSC_code,Balance):        
     self.AccountNo=AccountNo
     self.AccountName=AccountName
     self.IFSC_code=IFSC_code
     self.Balance=Balance
    def dispaly(self):
     print(" AccountNo:{}\n AccountName:{}\n IFSC_code:{}\n Balance:{}\n".format(self.AccountNo,self.AccountName,self.IFSC_code,self.Balance))
Account1=BankingAccount(12344559,'MOHAN','VDL0987',17000)
Account1.dispaly()
'''
#TO ADD WITHDRAW AND DEPOSIT ,CHECK BALANCE


class BankingAccount:
    def __init__(self,AccountNo,AccountName,IFSC_code,Balance):        
     self.AccountNo=AccountNo
     self.AccountName=AccountName
     self.IFSC_code=IFSC_code
     self.Balance=Balance
    def withdraw(self,amount):
        self.Balance-=amount
    def deposit(self,amount):
        self.Balance+=amount
    def checkbalance(self):
        print(self.Balance)
     #print(" AccountNo:{}\n AccountName:{}\n IFSC_code:{}\n Balance:{}\n".format(self.AccountNo,self.AccountName,self.IFSC_code,self.Balance))
Account1=BankingAccount(12344559,'MOHAN','VDL0987',7000)
Account1.deposit(3000)
