sayi1=int(input("1. Sayı:"))
sayi2=int(input("2. Sayı:"))
islem=input("İşlemi seçiniz, + - / *   ")
if islem=="+":
    print("sonuç=",sayi1+sayi2)
elif islem=="-":
    print("sonuç=",sayi1-sayi2)
elif islem=="/":
    print("sonuç=",sayi1/sayi2)
elif islem=="*":
    print("sonuç=",sayi1*sayi2)
else:
    print("Hatalı işlem girdiniz")
