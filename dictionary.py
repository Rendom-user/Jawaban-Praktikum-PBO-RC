jumlah_siswa = int(input("jumlah siswa : "))

dictionary = {}
for i in range (jumlah_siswa):

    nama = input("nama siswa : ")

    nilai = int (input ("nilai siswa : "))

    dictionary[nama] = nilai

print (end = "\n")

print ("dictiorary : ",( dictionary))
