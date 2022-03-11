#girilen öğrenci sayısı kadar notun ortalamasını alan program
toplamNot=0
ogrSay=int(input("Öğrenci Sayısı="))
for i in range(1,ogrSay+1):
    puan=int(input("Öğrenci notu="))
    toplamNot=toplamNot+puan
print("Öğrencilerin ortalaması=",toplamNot/ogrSay)
