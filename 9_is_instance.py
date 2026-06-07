class Karyawan :
    def __init__(self, nama) :
        self.nama = nama

class KaryawanTetep(Karyawan) :
    def __init__(self, nama):
        self.nama = nama

class Manager(Karyawan) :
    def __init__(self, nama):
        self.nama = nama

class Outsoursing :
    def __init__(self, nama):
        self.nama = nama

eko = Karyawan("eko")
ismail = KaryawanTetep("ismail")
rizka = Manager("rizka")
hasan = Outsoursing("hasan")

print(isinstance(eko, Karyawan))
print(isinstance(ismail, Karyawan))
print(isinstance(rizka, Karyawan))
print(isinstance(hasan, Karyawan))