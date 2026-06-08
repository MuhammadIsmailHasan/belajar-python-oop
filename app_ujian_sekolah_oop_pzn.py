import random

class Soal :
    def __init__(self, soal_text, jawaban_list, jawaban_benar):
        self.soal_text = soal_text
        self.jawaban_benar = jawaban_benar
        self.jawaban_list = jawaban_list

        random.shuffle(self.jawaban_list)

    def check_jawaban(self, jawaban_user):
        return True if jawaban_user == self.jawaban_benar else False

class SoalUjian :
    _data_soal_list = []
    soal_list = []

    def __init__(self, file, jumlah_soal):
        self.file = file
        self.jumlah_soal = jumlah_soal

    def ambil_soal(self):
        with open(self.file, "r") as file:
            for i in file:
                self._data_soal_list.append(i)

    def acak_soal(self):
        self.ambil_soal()
        random.shuffle(self._data_soal_list)

        for i in range(self.jumlah_soal):
            soal_jawaban = self._data_soal_list[i].split("|")

            jawaban_list = soal_jawaban[1].strip().split(",")
            jawaban_benar = jawaban_list[0]

            soal = Soal(soal_jawaban[0], jawaban_list, jawaban_benar)
            self.soal_list.append(soal)

class Ujian :
    _nilai = 0

    def __init__(self, file, jumlah_soal):
        self.jumlah_soal = jumlah_soal
        self.file = file

    def nilai(self):
        return self._nilai

    def run(self):
        urutan_jawaban = ["a", "b", "c", "d"]

        soal = SoalUjian(self.file, self.jumlah_soal)
        soal.acak_soal()

        for i in range(len(soal.soal_list)):
            soal_ujian = soal.soal_list[i]
            print(f"({i + 1}). {soal_ujian.soal_text}")

            for j in range(len(soal_ujian.jawaban_list)):
                print(f"{urutan_jawaban[j]}. {soal_ujian.jawaban_list[j]}")

            jawaban_user = input("masukan jawaban anda (a/b/c/d) : ")
            if jawaban_user in urutan_jawaban:
                index_jawaban_user = urutan_jawaban.index(jawaban_user)

                soal_obj = soal_ujian.check_jawaban(soal_ujian.jawaban_list[index_jawaban_user])
                if soal_obj :
                    self._nilai += 10
            else:
                print("pilihan tidak valid")

        print(f"nilai anda : {self._nilai}")


if __name__ == "__main__":
    app = Ujian("soal.txt", 5)
    app.run()
    print("Ujian selesai")
