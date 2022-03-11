saat=int(input("Saati giriniz:"))
if saat>=7 and saat<12:
    print("Günaydın")
elif saat>=12 and saat<17:
    print("Tünaydın")
elif saat>=17 and saat<20:
    print("İyi Akşamlar")
elif (saat>=20 and saat<=24) or (saat>=0 and saat<7) :
    print("İyi Geceler")
else:
    print("Yanlış saat girişi yaptınız")
