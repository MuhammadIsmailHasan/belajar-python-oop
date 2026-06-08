import random

class SoalUjian :
    _data_soal_list = []
    jumlah_soal = 0

    def __init__(self, jumlah_soal):
        self.jumlah_soal = jumlah_soal

    @property
    def data_soal_list(self):
        return self._data_soal_list

    def ambil_soal(self):
        with open("soal.txt", "r") as file:
            for i in file:
                self._data_soal_list.append(i)

    def acak_soal(self):
        self.ambil_soal()
        random.shuffle(self._data_soal_list)

        soal_list = []
        for i in range(self.jumlah_soal):
            soal_jawaban = self._data_soal_list[i].split("|")

            jawaban_list = soal_jawaban[1].strip().split(",")
            jawaban_benar = jawaban_list[0]
            random.shuffle(jawaban_list)

            soal_list.append({
                "soal": soal_jawaban[0],
                "jawaban": jawaban_list,
                "jawaban_benar": jawaban_benar
            })

        return soal_list

class Ujian :
    _nilai = 0
    urutan_jawaban = ["a", "b", "c", "d"]

    def __init__(self, jumlah_soal):
        self.jumlah_soal = jumlah_soal

    def nilai(self):
        return self._nilai

    def do_ujian(self):
        soal = SoalUjian(self.jumlah_soal)
        soal_ujian = soal.acak_soal()

        for i in range(len(soal_ujian)):
            print(f"({i + 1}). {soal_ujian[i]['soal']}")

            for j in range(len(soal_ujian[i]['jawaban'])):
                print(f"{self.urutan_jawaban[j]}. {soal_ujian[i]['jawaban'][j]}")

            jawaban_user = input("masukan jawaban anda (a/b/c/d) : ")
            if jawaban_user in self.urutan_jawaban:
                index_jawaban_user = self.urutan_jawaban.index(jawaban_user)

                if (soal_ujian[i]['jawaban_benar'] == soal_ujian[i]['jawaban'][index_jawaban_user]):
                    self._nilai += 10
            else:
                print("pilihan tidak valid")



ujian = Ujian(5)
ujian.do_ujian()
print(ujian.nilai())