class MiniBank :
    _rekening_number = ""
    __pin_number = 123456
    __balance = 10000000
    __is_verified = False
    _is_active = True

    def __init__ (self, rekening_number) :
        self._rekening_number = rekening_number

    @property
    def rekening_number(self):
        return self._rekening_number

    @property
    def balance(self):
        if (self.__is_verified):
            return self.__balance
        else:
            raise PermissionError("Wrong pin number!")

    def submit_pin(self, pin):
        if pin == self.__pin_number :
            self.__is_verified = True
            print("Pin verified")
            return True
        else :
            self.__is_verified = False
            print("Pin not verified")
            return False

    def topup(self, amount):
        if (self.__is_verified) :
            self.__balance += amount
            return amount
        else :
            raise PermissionError("Not Accessable, wrong pin number!")

    def cashout(self, amount):
        if (self.__is_verified) :
            if (self.__balance < amount) :
                raise ValueError("Not enough money")
            self.__balance -= amount
            return amount
        else :
            raise PermissionError("Not Accessable, wrong pin number!")

bank_bri = MiniBank("99999")
bank_bri.submit_pin(123456)
print(bank_bri.balance)
print(bank_bri.topup(30000))
print(bank_bri.balance)
bank_bri.cashout(1000)
print(bank_bri.balance)

bank_bri.rekening_number = "2000000"


