saniye=int(input("Saniye değerini giriniz >"))
dakika=saniye//60
kalansaniye=saniye%60
saat=dakika//60
kalandakika=dakika%60
gun=saat//24
kalansaat=saat%24
print(saniye,"saniye eşittir",gun,"gün",kalansaat,"saat",kalandakika,"dakika",kalansaniye,"saniyedir")
