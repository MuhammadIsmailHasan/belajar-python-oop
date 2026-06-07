# harus inherintance dari class Exception 

class BalanceNotEnough(Exception) :
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class Bank() :
    def __init__(self, rekening_number, balance=0):
        self.rekening_number = rekening_number
        self.balance = balance

    def cashout(self, amount):
        if amount > self.balance :
            raise BalanceNotEnough("Balance Not Enough")
        else :
            self.balance -= amount

try :
    bank_bca = Bank(12345, 1000)
    bank_bca.cashout(2000)

except BalanceNotEnough as error :
    print(f"Error: {error}")

print("Program selesai!")