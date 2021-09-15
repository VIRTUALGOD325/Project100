class ATM():
    def __init__(self):
        self.self = self

    def access(self):
        pin = input("ENTER YOUR PIN TO START: ")
        print(pin)
        print("ACCESS GRANTED")

    def cashWithdraw(self):
        amount = input("HOW MUCH DO YOU WANT TO WITHDRAW: ")
        print("AMOUNT WITHDRAWN",amount)
        print("Transaction complete")

    def depositcash(self):
        amount2 = input("HOW MUCH DO YOU WANT TO DEPOSIT: ")
        print("AMOUNT DEPOSITED",amount2)
        print("Transaction complete")        

xyz = ATM()
xyz.access()
xyz.cashWithdraw()
xyz.depositcash()