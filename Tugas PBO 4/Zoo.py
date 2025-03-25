from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age):
        if not name:
            raise ValueError("Nama hewan tidak boleh kosong.")
        if age <= 0:
            raise ValueError("Usia hewan harus lebih dari 0.")
        
        self.__name = name
        self.__age = age
    
    @abstractmethod
    def make_sound(self):
        pass
    
    def get_info(self):
        return f"Nama : {self.__name}, Usia : {self.__age} tahun"
    
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def set_age(self, new_age):
        if new_age <= 0:
            raise ValueError("Usia hewan harus lebih dari 0.")
        self.__age = new_age

class Zoo:
    def __init__(self):
        self.animals = []
    
    def add_animal(self, animal):
        if not isinstance(animal, Animal):
            raise TypeError("Objek yang dimasukkan bukan hewan yang valid.")
        self.animals.append(animal)
        print(f"{animal.get_name()} berhasil ditambahkan ke kebun binatang!")
    
    def show_animals(self):
        if not self.animals:
            print("Tidak ada hewan di kebun binatang.")
        else:
            print("Daftar Hewan di Kebun Binatang :")
            for animal in self.animals:
                print(f"- {animal.get_info()} | Suara : {animal.make_sound()}")

def main():
    zoo = Zoo()
    hewan_terdaftar = {}
    
    while True:
        print("\nPilih aksi :")
        print("1. Tambah Hewan")
        print("2. Tampilkan Hewan")
        print("3. Keluar")
        pilihan = input("Masukkan pilihan (1/2/3) : ")
        
        if pilihan == "1":
            try:
                jenis = input("Masukkan jenis hewan : ").strip().lower()
                nama = input("Masukkan nama hewan : ").strip()
                usia = int(input("Masukkan usia hewan : "))
                
                if jenis not in hewan_terdaftar:
                    class CustomAnimal(Animal):
                        def make_sound(self):
                            return input(f"Masukkan suara untuk {jenis} : ")
                    hewan_terdaftar[jenis] = CustomAnimal
                
                hewan = hewan_terdaftar[jenis](nama, usia)
                zoo.add_animal(hewan)
            except ValueError as e:
                print(f"Error : {e}")
        elif pilihan == "2":
            zoo.show_animals()
        elif pilihan == "3":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()