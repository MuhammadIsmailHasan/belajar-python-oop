# jika dalam polimorphsm harus extend dari kelas parent
# dalam python ini tidak perlu
# asalkan dalam class tersebut punya method yang sama, entah itu punya parent yg sama atau tidak
# maka akan tetap dijalankan

# JIKA DALAM POLYMORPHSM MEMBUTUHKAN INHERITANCEH
# DUCK TYPING TIDAK PERLU ITU

class Bebek :
    def suara (self) :
        print("suara bebek")

class Kucing :
    def suara (self) :
        print("suara kucing")

class Anjing :
    def suara (self) :
        print("suara anjing")

class Mobil :
    def nyalakan(self) :
        print("nyalakan mobil")

bebek = Bebek()
kucing = Kucing()
anjing = Anjing()
avanza = Mobil()

barang_list = [
    bebek,
    kucing,
    anjing,
    # avanza # error karena tidak punya method suara
]

for barang in barang_list :
    barang.suara()