# MENGGUNAKAN GETTER SETTER MANUAL
class Mahasiswa :
    _nim = ""
    # tanda _ artinya attribute tidak boleh di akses langsung

    def set_nim (self, nim) :
        if nim == "" :
            raise ValueError("Nim is empty")
        self._nim = nim

    def get_nim (self) :
        return self._nim

ismail = Mahasiswa()
ismail.set_nim("12345")
print(ismail.get_nim())


# MENGGUNAKAN PROPERTY METHOD
class Siswa :
    _nisn = ""

    @property
    def nisn(self) :
        return self._nisn
    # ini adalah getternya
    # bisa memanggil langsung object.nisn, TANPA HARUS PAKAI KURUNG SEPERTI nisn()

    @nisn.setter
    def nisn (self, nisn) :
        if nisn == "" :
            raise ValueError("NISN is empty")

        self._nisn = nisn
    # ini adalah setternya

rizka = Siswa()
rizka.nisn = "10101010" # mirip seperti mengakses attribute kaaaann
print(rizka.nisn)




