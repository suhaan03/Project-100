class atm(object):
    def __init__(self,name,cardno,pinno):
        self.name = name
        self.cardno = cardno
        self.pinno = pinno

    def  CashWithdrawl(self):
        print("Enter the amount for withdrawl")
        

    def BalanceEnquiry(self):
        print("Check the amount remaining in your account")

jack = atm("jack", 1414262683527549, 7899)

print(jack.CashWithdrawl())
print(jack.BalanceEnquiry())