
#Back account management
class Account:
    def __init__(self,name,age: int,idNumber: int, Balance: int):
        self.name = name
        self.age = age
        self.idNumber = idNumber
        self.__Balance = Balance
    def modifyBalance(self):
        #tinh dong goi
        self.__Balance = 1000000
    def information(self):
        return self.idNumber,self.name,self.age,self.__Balance
test = Account('hung',22,23432434,345151.13)

#changedInfor = test.modifyBalance()
#print information
infor = test.information()
print(infor)


# In[98]:

#tinh ke thua
class foreignAccount(Account):
    exchanged = int
    def __init__(self,name,age: int,idNumber: int, Balance: int, currency: str):
        super().__init__(name,age,idNumber,Balance)
        self.Balance = Balance
        self.currency = currency 
    def convertCurrency(self):
        self.exchanged = self.Balance * self.currency
        return self.exchanged
    def information(self):
        return f"{self.idNumber} \n{self.name} \n{self.age} \nBalance's amount in VN currency is: {self.Balance} \nExchanged money to dollar with rate of {self.currency} is : {self.exchanged}"
test1 = foreignAccount('alex',25,23232434,311151.13,22.3)
changedAmount = test1.convertCurrency()
infor1 = test1.information()
print(infor1)





