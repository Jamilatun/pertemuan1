print('''Program Menghitung Nilai Rata - Rata
========================================''')
#variabel bernama jumlahBilangan akan diinisialisasi dengan nilai yang diinput oleh pengguna melalui fungsi input(). Fungsi int() akan mengubah nilai yang diinput menjadi tipe data integer (bilangan bulat).

jumlahBilangan = int(input("-- Masukkan banyaknya data :"))

#Membuat garis baru
print()

#Program perhitungan dan perulangan
angka = [] #merupakan sebuah perintah untuk membuat sebuah objek list kosong dengan nama "angka".
jumlah = 0 #variabel jumlah berisi nol
for i in range (0, jumlahBilangan): #merupakan perintah perulangan (loop) yang akan mengeksekusi sekumpulan perintah di dalam blok perulangan sebanyak jumlah kali yang ditentukan.
    inpt = int(input("Masukkan Angka ke-%d: " % (i+1))) # untuk meminta input dari pengguna dan mengubahnya menjadi tipe integer (bilangan bulat). 
    angka.append(inpt) #menambahkan item ke dalam sebuah list. 
    jumlah += angka[i] #menambahkan item ke dalam sebuah variabel. 
    rata2 = jumlah / jumlahBilangan #menghitung rata-rata dari sejumlah bilangan.


#Membuat garis baru
print()

#Mencetak hasil rata2
print("-- Rata-rata = %0.2f" % rata2)

print('''========================================''')
