class BankAccount :
    number = 0
    balance = 0
    is_active = True

    # construktor
    def __init__ (self, number, balance) :
        self.number = number
        self.balance = balance

    # digunakan untuk seperti membuat object dari class itu sendiri
    # atau instance dari method 
    @classmethod
    def deactivate (cls, number, balance) :
        result = cls(number, balance) # ini memanggil konstruktor
        result.is_active = False
        return result

# tanpa class method
bank_bri = BankAccount(123, 1000)
bank_bri.is_active = False
print(f"number : {bank_bri.number}, balance : {bank_bri.balance}, bank_bri.is_active : {bank_bri.is_active}")

# dengan class method
bank_bca = BankAccount.deactivate(456, 2000)
print(f"number : {bank_bca.number}, balance : {bank_bca.balance}, bank_bca.is_active : {bank_bca.is_active}")
