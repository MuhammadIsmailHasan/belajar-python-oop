# ATTRIBUTE DALAM CLASS
class Kampus:
    nama = ""
    jurusan = ""

kampus1 = Kampus()
kampus1.nama = "UIN"
kampus1.jurusan = "Teknik Informatika"

kampus2 = Kampus()

print("== attribute ==")
print(kampus1.nama)
print(kampus1.jurusan)

# error karena attribute nama menempel di object kampus1
# ini disebut instance object, dimana atribute tidak ada di class tapi langsung di definisikan di object
# labih aman, attribute di definisikan di class
print(kampus2.nama)
print(type(kampus1))



# METHOD DALAM CLASS
# self SANGAT PENTING DALAM METHOD, harus ada karena digunakan untuk mengakses object tersebut
class Mahasiswa:
    nim = ""
    alamat = ""

    def perkenalan(self):
        print(f"halo {self.nim}")

    def hello(self, nama):
        print(f"hallo {nama}, alamat anda: {self.alamat}")

print("== method ==")
ismail = Mahasiswa()
ismail.perkenalan()

ismail.hello("ismail hasan")



