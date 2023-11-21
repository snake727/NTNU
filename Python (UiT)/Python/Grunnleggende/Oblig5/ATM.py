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

def main():
    accounts = []
    #Creates 10 accounts as the assignment asked for
    for i in range(0, 9):
        account = Account(i, 100)
        accounts.append(account)

    while True:
        accountid = int(input("Please enter an account ID: "))

        #Ensures that we stay within our valid accounts
        while accountid < 0 or accountid > 9:
            accountid = int(input("\nEnter valid account number: "))

        #Implemented function getAChoice() given in assignment in Canvas
        while True:
            print("\nMain menu")
            print("1: check balance")
            print("2: withdraw")
            print("3: deposit")
            print("4: exit")
            print("Enter a choice: ", end = "")
            choice = int(input())

            #Modification allowing for selecting correct account when input
            for acc in accounts:
                if acc.getId() == accountid:
                    accountObj = acc
                    break

            if choice < 1 or choice > 4:
                print("Invalid choice, try again: ", end = "")
            else:
                if choice == 1:
                    print(f"The balance is {accountObj.getBal()}")
                elif choice == 2:
                    amount = float(input("Enter an amount to withdraw: "))
                    if amount > accountObj.getBal():
                        print("Insufficient funds!")
                    else:
                        accountObj.withdraw(amount)
                elif choice == 3:
                    amount = float(input("Enter an amount to deposit: "))
                    accountObj.deposit(amount)
                elif choice == 4:
                    break
main()