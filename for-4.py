#1'den 10'a kadar olan sayıları toplayan program
toplam=0
ilk=int(input("Başlangıç değeri:"))
son=int(input("Son değer:"))
for sayac in range(ilk,son+1):
    toplam=toplam+sayac
print("Sayıların toplamı=",toplam)
