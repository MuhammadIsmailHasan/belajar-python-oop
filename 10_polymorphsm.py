class Remote :
    def __init__(self, nama):
        self._nama = nama

    @property
    def nama(self) :
        return self._nama

class Ac(Remote) :
    def nyalakan(self):
        print("Nyalakan AC")

class Tv(Remote) :
    def nyalakan(self):
        print("Nyalakan TV")

class Kompor(Remote) :
    def nyalakan(self):
        print("Nyalakan Kompor")

class MagicCom(Remote) :
    pass

elektronika_list = [
    Ac("angin"),
    Tv("gambar"),
    Kompor("api"),
    # MagicCom("uap") # ini error karena class tersebut tidak punya method nyalakan
]

for e in elektronika_list :
    e.nyalakan()
    print(f"berbentuk : {e.nama}")