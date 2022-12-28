number1 = 5
number2 = 10

#operator perbandingan

if number1 != number2:
    print("nomor berbeda")
else :
    print("nomor sama")


#operator logika
if number1 > 99 and number1 < 1000:
    print("bilangan ratusan")
else:
    print("bukan bilangan ratusan")

#operator aritmatika
while True:
    number3 = int(input("masukan angka : "))

    if number3 == 00:
        break
    if number3 % 2 == 0 :
        print("bilangan genap")
    else:
        print("bilangan ganjil")