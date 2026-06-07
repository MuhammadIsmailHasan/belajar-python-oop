# tanpa static method

class Matematika :
    def tambah(self, a, b):
        return a + b

pertambahan = Matematika()
print(pertambahan.tambah(2,3))

# dengan static method
class MatematikaStatic :

    @staticmethod
    def tambah(a, b):
        return a + b

print(MatematikaStatic().tambah(2,5))
# method dapat di akses tambah pembuatan object terlebih dahulu