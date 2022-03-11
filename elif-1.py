#Girilen notun karşılığı olan sözel ifadeye çeviren program
ort=int(input("Not ortalamasını giriniz :"))
if ort>=0 and ort<45:
    print("Zayıf")
elif ort<55 and ort>44:
    print("Geçer")
elif ort<70 and ort>54:
    print("Orta")
elif ort<85 and ort>69:
    print("İyi")
elif ort<101 and ort>84:
    print("Pekiyi")
else:
    print("Düzgün not gir...!")
        
