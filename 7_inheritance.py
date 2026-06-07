class Kendaraan :
    def __init__(self, merk, tahun_pembuatan):
        self.merk = merk
        self.tahun_pembuatan = tahun_pembuatan

    def info(self):
        print(f"ini adalah {self.merk} dengan tahun pembuatan {self.tahun_pembuatan}")

    def nyalakan(self):
        print("Nyalakan mesin kendaraan")


class Mobil(Kendaraan):

    def __init__(self, merk, tahun_pembuatan, jumlah_roda):
        super().__init__(merk, tahun_pembuatan) # menambahkan super agar bisa mengakses method dari parent
        self.jumlah_roda = jumlah_roda

    def info(self):
        print("ini adalah info dari child")

    def info_parent(self):
        super().info()

    def klakson(self):
        print(f"mobil mempunyai klakson")

    # method overriding
    def nyalakan(self):
        print(f"motor {self.merk} di nyalakan dari child")


class Motor(Kendaraan):
    def klakson(self):
        print("motor mempunyai klakson")


avanza = Mobil("avanza", 2020, 4)
avanza.klakson()
avanza.info()
avanza.info_parent()
avanza.nyalakan()

supra = Motor("supra", 2025)
supra.klakson()