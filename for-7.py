#Öğrenci sayısına göre not ortalamasını bulan program
toplamNot=0
girilen=0
ogrSay=int(input("Öğrenci sayısı:"))
for sayac in range(1,ogrSay+1):
    print(sayac,". Öğrenci")
    ogrNot=int(input("Öğrenci Notu="))
    girilen=girilen+1
    print("toplam notu girilen öğrenci=",girilen)
    toplamNot=toplamNot+ogrNot
print("Not ortalaması=",toplamNot/girilen)

