#klavyeden 5 öğrenci için girilen notların ortalamasını alan program
toplamNot=0

for i in range(1,6):
    dersNotu=int(input("Öğrecinin notu="))
    toplamNot=toplamNot+dersNotu
    
ort=toplamNot/5
print("Girilen notların ortalaması=",ort)
