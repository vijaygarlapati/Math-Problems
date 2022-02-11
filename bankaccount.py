#Simple Bank account class
class BankAccount():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,dep):
        self.balance = self.balance + dep
        print(f"Added Rs.{dep}")
        print("Thank you for depositing amount! Total account balance is: Rs.{} ".format(self.balance))
    def withdrawl(self,wdwl):
        #wdwl = int(input("Enter the withdrawl amount:"))
        if self.balance>=wdwl:
            self.balance = self.balance -wdwl
            print("withdrawl is accepted and your total account balance is: Rs.{}".format(self.balance))
        else:
            print("withdrawl is denied due to insufficient balance")
