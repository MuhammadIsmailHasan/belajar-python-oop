# digunakan untuk operasi antar objek dengan objek
# tipa obj1 + obj2, maka akan bingung karena python tidak tau hal apa yang diproses/ditambahkan dalam operasi tersebut

# jumlah_uang_obj_kedua, kembali pada object kedua yang memiliki atribute _jumlah_uang
# bisa di return dengan variable atau class itu sendiri

"""
    __add__ untuk +
    __sub__ untuk -
    __mul__ untuk *
    __eq__ untuk ==
    __lt__ untuk < (less than)
    __gt__ untuk > (greater then)
    __le__ untuk <= (less equal)
    __ge__ untuk >= (greater equal)
    __ne__ untuk !=
"""

class Dompet :
    def __init__(self, jumlah_uang) :
        self._jumlah_uang = jumlah_uang

    @property
    def jumlah_uang(self) :
        return self._jumlah_uang

    def __add__ (self, jumlah_uang_obj_kedua) :
        total_uang = self._jumlah_uang + jumlah_uang_obj_kedua._jumlah_uang
        return total_uang

    def __sub__ (self, jumlah_uang_obj_kedua) :
        pengurang = self._jumlah_uang - jumlah_uang_obj_kedua._jumlah_uang
        return Dompet(pengurang)

ismail = Dompet(1000000)
rizka = Dompet(500000)

total = ismail + rizka
print(total)
print(type(total))


kurang = ismail - rizka
print(kurang.jumlah_uang)
print(type(kurang))