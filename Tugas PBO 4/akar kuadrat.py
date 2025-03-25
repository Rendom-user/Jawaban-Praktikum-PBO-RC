import math

def hitung_akar():
    while True:
        try:
            angka = input("Masukkan angka : ")
            angka = float(angka)  # Mengonversi input ke float
            
            if angka < 0:
                print("Erorr, masukkan angka .")
            elif angka == 0:
                print("Error 0.")
            else:
                hasil = math.sqrt(angka)
                print(f"Akar kuadrat dari {angka} adalah {hasil:.2f}")
                break  # Keluar dari loop jika input valid
        except ValueError:
            print("Error.")

# Menjalankan program
hitung_akar()
