class Kendaraan:
    def __init__(self, jenis, kecepatan_maksimum):
        self.jenis = jenis
        self.kecepatan_maksimum = kecepatan_maksimum

    def info_kendaraan(self):
        return f"Jenis Kendaraan : {self.jenis} \nTop Speed : {self.kecepatan_maksimum} km/jam\n"
    
    def bergerak(self):
        return "Kendaraan bergerak maju"

class Mobil(Kendaraan):
    def __init__(self, merk, jumlah_pintu, jenis, kecepatan_maksimum):
        super().__init__(jenis, kecepatan_maksimum)
        self.merk = merk
        self.jumlah_pintu = jumlah_pintu
    
    def info_mobil(self):
        return f"Merk : {self.merk} \nJumlah Pintu : {self.jumlah_pintu}\n"

    def bunyikan_klakson(self):
        return "Beep Beep!"

class MobilSport(Mobil):
    def __init__(self, merk, jumlah_pintu, jenis, kecepatan_maksimum, tenaga_kuda, harga):
        super().__init__(merk, jumlah_pintu, jenis, kecepatan_maksimum)
        self.__tenaga_kuda = tenaga_kuda
        self.__harga = harga

    def get_tenaga_kuda(self):
        return f"Horse Power : {self.__tenaga_kuda} HP\n"

    def set_tenaga_kuda(self, value):
        self.__tenaga_kuda = value
    
    def get_harga(self):
        return f"Harga : Rp {self.__harga} juta\n"

    def set_harga(self, value):
        self.__harga = value
    
    def info_mobil_sport(self):
        return f"Merk: {self.merk}\nJumlah Pintu : {self.jumlah_pintu}\n" \
               f"Horse Power : {self.__tenaga_kuda} HP\nHarga : Rp {self.__harga} juta\n"

    def mode_balap(self):
        return "Sport mode ON!"

MobilSport1 = MobilSport("Supra", 2, "Darat", 300, 500, 1000000)

print(MobilSport1.info_kendaraan())
print(MobilSport1.bergerak())
print(MobilSport1.info_mobil())
print(MobilSport1.bunyikan_klakson())
print(MobilSport1.info_mobil_sport())
print(MobilSport1.get_tenaga_kuda())
print(MobilSport1.get_harga())
print(MobilSport1.mode_balap())
