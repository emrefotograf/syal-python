#öğrenci sayısı kadar notun ortalamasını alan program
toplamPuan=0
ogrSay=int(input("Öğrenci Sayısı:"))
for i in range(1,ogrSay+1):
    ogrNot=int(input("Notu giriniz:"))
    toplamPuan=toplamPuan+ogrNot
    print("Not eklendi"
        
print("Notların Ortalaması=",toplamPuan/ogrSay)


