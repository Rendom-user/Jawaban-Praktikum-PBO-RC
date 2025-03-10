
nama = input("Masukkan nama : ")
nim = input("Masukkan NIM : ")
resolusi = input("Masukkan Resolusi di Tahun ini : ")


with open("Me.txt", "w") as file :
    file.write(f"Nama: {nama}\n")
    file.write(f"NIM: {nim}\n")
    file.write(f"Resolusi Tahun Ini: {resolusi}\n")

print('File "Me.txt" telah berhasil dibuat!')
