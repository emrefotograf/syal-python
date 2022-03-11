ort=int(input("Ders ortalamasını giriniz:"))
if ort>=0 and ort<45:
    print("Zayıf")
elif ort>44 and ort<55:
    print("Geçer")
elif ort>54 and ort<70:
    print("Orta")
elif ort>69 and ort<85:
    print("İyi")
elif ort>84 and ort<=100:
    print("Pekiyi")
else:
    print("Yanlış not girişi!")

