#klavyeden girilen sayıya kadar sayıları toplayan program
#Programı yazan SYAL
toplam=0
sayi=int(input("Sayıyı giriniz :"))
for sayac in range(1,sayi+1):
    toplam=toplam+sayac
print("istenilen aralıktaki sayıların toplamı =",toplam)
