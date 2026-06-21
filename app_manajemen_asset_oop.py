class Aset :
    def __init__(self, kode, nama, harga):
        self.kode = kode
        self.nama = nama
        self.harga = harga

class Kendaraan(Aset) :
    def __init__(self, kode, nama, harga, nopol, tahun):
        super().__init__(kode, nama, harga)
        self.nopol = nopol
        self.tahun = tahun

class Bangunan(Aset) :
    def __init__(self, kode, nama, harga, tipe_bangunan, luas):
        super().__init__(kode, nama, harga)
        self.tipe_bangunan = tipe_bangunan
        self.luas = luas

class Elektronik(Aset) :
    def __init__(self, kode, nama, harga, serial_number, jenis):
        super().__init__(kode, nama, harga)
        self.serial_number = serial_number
        self.jenis = jenis

class DaftarAset() :
    def __init__(self):
        self.daftar_aset = []

    def tambah(self, aset):
        self.daftar_aset.append(aset)

    def ambil_by_kode(self, kode):
        for aset in self.daftar_aset :
            if aset.kode == kode:
                return aset
        else :
            return None

    def hapus_by_kode(self, kode):
        for index, aset in enumerate(self.daftar_aset):
            if aset.kode == kode :
                del self.daftar_aset[index]
                return True
        return False

class AplikasiManajemenAset() :
    def __init__(self):
        self.daftar_aset_obj = DaftarAset()

    def run(self):
        while(True):
            print("== APLIKASI MANAJEMEN MENU UTAMA == ")
            print("1. LIHAT DAFTAR ASET")
            print("2. TAMBAH ASET")
            print("3. KELUAR")

            user_menu_selected = int(input("Masukan menu yang anda pilih : "))
            if user_menu_selected == 1:
                self.run_lihat_aset()
            elif user_menu_selected == 2:
                self.run_tambah_aset()
            elif user_menu_selected == 3:
                break

    def run_tambah_aset(self):
        while(True):
            print("-- Menambahkan aset -- ")
            print("1. tambah kendaraan")
            print("2. tambah bangunan")
            print("3. tambah elektronik")
            print("4. kembali ke menu utama")

            user_tambah_aset_selected = int(input("Ingin menambahkan aset berupa : "))
            if user_tambah_aset_selected == 1:
                self.run_tambah_aset_kendaraan()
            elif user_tambah_aset_selected == 2:
                self.run_tambah_aset_bangunan()
            elif user_tambah_aset_selected == 3:
                self.run_tambah_aset_elektronik()
            elif user_tambah_aset_selected == 4:
                break

    def run_tambah_aset_kendaraan(self):
        kode_input = input("Masukan kode kendaraan: ")
        nama_input = input("Masukan nama kendaraan: ")
        harga_input = input("Masukan harga kendaraan: ")
        nopol_input = input("Masukan nopol kendaraan: ")
        jenis_input = input("Masukan jenis kendaraan: ")

        kendaraan = Kendaraan(kode_input, nama_input, harga_input, nopol_input, jenis_input)
        self.daftar_aset_obj.tambah(kendaraan)

    def run_tambah_aset_bangunan(self):
        kode_input = input("Masukan kode bangunan: ")
        nama_input = input("Masukan nama bangunan: ")
        harga_input = input("Masukan harga bangunan: ")
        tipe_bangunan_input = input("Masukan tipe_bangunan: ")
        luas_input = input("Masukan luas bangunan: ")

        bangunan = Bangunan(kode_input, nama_input, harga_input, tipe_bangunan_input, luas_input)
        self.daftar_aset_obj.tambah(bangunan)

    def run_tambah_aset_elektronik(self):
        kode_input = input("Masukan kode elektronik: ")
        nama_input = input("Masukan nama elektronik: ")
        harga_input = input("Masukan harga elektronik: ")
        serial_number_input = input("Masukan serial_number elektronik: ")
        jenis_input = input("Masukan jenis elektronik: ")

        elektronik = Elektronik(kode_input, nama_input, harga_input, serial_number_input, jenis_input)
        self.daftar_aset_obj.tambah(elektronik)

    def daftar_aset_kendaraan(self, aset):
        print("## DAFTAR KENDARAAN ##")
        print("kode : ", aset.kode)
        print("nama : ", aset.nama)
        print("harga : ", aset.harga)
        print("nopol : ", aset.nopol)
        print("tahun : ", aset.tahun)
        print()

    def daftar_aset_bangunan(self, aset):
        print("## DAFTAR BANGUNAN ##")
        print("kode : ", aset.kode)
        print("nama : ", aset.nama)
        print("harga : ", aset.harga)
        print("tipe bangunan : ", aset.tipe_bangunan)
        print("luas : ", aset.luas)
        print()

    def daftar_aset_elektronik(self, aset):
        print("## DAFTAR ELEKTRONIK ##")
        print("kode : ", aset.kode)
        print("nama : ", aset.nama)
        print("harga : ", aset.harga)
        print("serial number : ", aset.serial_number)
        print("jenis : ", aset.jenis)
        print()

    def run_lihat_aset(self):
        for aset in self.daftar_aset_obj.daftar_aset:
            if (isinstance(aset, Kendaraan)) :
                self.daftar_aset_kendaraan(aset)
            elif(isinstance(aset, Bangunan)) :
                self.daftar_aset_bangunan(aset)
            elif(isinstance(aset, Elektronik)) :
                self.daftar_aset_elektronik(aset)

        # menu setelah lihat aset
        print("-- Menu Pengolahan Aset --")
        print("1. Ubah ?")
        print("2. Hapus ?")
        print("3. Kembali ke menu utama")
        user_lihat_selected = int(input("Ingin mengolah apa : "))
        if (user_lihat_selected == 1):
            self.run_ubah_aset()
        elif (user_lihat_selected == 2):
            self.run_hapus_aset()

    def run_ubah_aset(self):
        user_kode_input = input("Masukan kode aset yang ingin diubah : ")
        aset = self.daftar_aset_obj.ambil_by_kode(user_kode_input)

        if aset is None :
            print("Kode aset tersebut tidak terlihat!")
        else :
            if isinstance(aset, Kendaraan) :
                # kendaraan
                nama_input = input("Masukan nama kendaraan: ")
                harga_input = input("Masukan harga kendaraan: ")
                nopol_input = input("Masukan nopol kendaraan: ")
                jenis_input = input("Masukan jenis kendaraan: ")
                aset.nama = nama_input
                aset.harga = harga_input
                aset.nopol = nopol_input
                aset.jenis = jenis_input
            elif isinstance(aset, Bangunan) :
                # bangunan
                nama_input = input("Masukan nama bangunan: ")
                harga_input = input("Masukan harga bangunan: ")
                tipe_input = input("Masukan tipe_bangunan: ")
                luas_input = input("Masukan luas bangunan: ")
                aset.nama = nama_input
                aset.harga = harga_input
                aset.tipe_bangunan = tipe_input
                aset.luas = luas_input
            elif isinstance(aset, Elektronik) :
                # elektronik
                nama_input = input("Masukan nama elektronik: ")
                harga_input = input("Masukan harga elektronik: ")
                serial_number_input = input("Masukan serial_number elektronik: ")
                jenis_input = input("Masukan jenis elektronik: ")
                aset.nama = nama_input
                aset.harga = harga_input
                aset.serial_number = serial_number_input
                aset.jenis = jenis_input

    def run_hapus_aset(self):
        user_kode_input = input("Masukan kode aset yang ingin : ")
        aset = self.daftar_aset_obj.hapus_by_kode(user_kode_input)

        if aset :
            print("Berhasil menghapus aset!")
        else :
            print("Gagal, kode tidak ditemukan!")

if __name__ == "__main__":
    aplikasi = AplikasiManajemenAset()
    aplikasi.run()