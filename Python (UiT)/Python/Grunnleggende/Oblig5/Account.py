class Account:
    def __init__(self, accId = 0, accBal = 100, accRate = 0):
        self.id = int(accId)
        self.balance = float(accBal)
        self.interestrate = float(accRate)
        self.monthlyinterestrate = float()
        self.monthlyinterest = float()

    #Getters
    def getId(self):
        return self.id

    def getBal(self):
        return self.balance
    
    def getRate(self):
        return self.interestrate

    #Setters
    def setId(self, accId):
        self.id = accId
    
    def setBal(self, accBal):
        self.balance = accBal
    
    def setRate(self, accRate):
        self.interestrate = accRate / 100
    
    #Other methods
    def getMonthlyInterestRate(self):
        self.monthlyinterestrate = self.interestrate / 12
        return self.monthlyinterestrate
    
    def getMonthlyInterest(self):
        self.monthlyinterest = self.monthlyinterestrate * self.balance
        return self.monthlyinterest

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance


TestAccount = Account()
TestAccount.setId(1122)
TestAccount.setBal(20000)
TestAccount.setRate(4.5)
TestAccount.withdraw(2500)
TestAccount.deposit(3000)

print(TestAccount.id)
print(TestAccount.balance)
print(TestAccount.interestrate)
print(TestAccount.getMonthlyInterestRate())
print(TestAccount.getMonthlyInterest())
