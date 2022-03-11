#öğrenci sayısı kadar notun ortalamasını alan program
notToplami=0
ogrSayisi=int(input("Öğrenci sayısını giriniz:"))
for i in range(1,ogrSayisi+1):
    print(i,"Öğrenci")
    puan=int(input("Puanı giriniz:"))
    notToplami=notToplami+puan
print("Not ortalaması=",notToplami/ogrSayisi)
    
