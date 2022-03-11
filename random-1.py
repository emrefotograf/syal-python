#rastgele sayı üreten program
import random
tutulan=random.randint(1,9)
for i in range(1,5):
    tahmin=int(input("Tahmininiz="))
    if tutulan==tahmin:
        print("Tebrikler,",i,". tahminde buldunuz.")
        hak=i
        break
    else:
        print("Tekrar deneyin...")
    if i==4:
        hak=5
        print("Tutulan Sayı=",tutulan)
print("Puanınız",100-(25*(hak-1)))
        
               
