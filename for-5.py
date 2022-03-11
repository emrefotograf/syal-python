#klavyeden girilen öğrenci sayısı kadar notun ortalamasını alan program
toplam=0
ogr=int(input("Öğrenci Sayısı:"))
for i in range(1,ogr+1):
    print(i,". Öğrenci notu :")
    oNotu=int(input())
    toplam=toplam+oNotu
ort=toplam/ogr
print("Tüm öğrencilerin not ortalaması=",ort)
