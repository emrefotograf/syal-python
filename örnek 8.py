saniye=int(input("Saniye cinsinden zamanı giriniz :"))
kalansaniye=saniye%60
#dakika=saniye//60
kalandakika=saniye//60%60
saat=saniye//3600%60
print(saniye,"saniye",saat,"saat",kalandakika,"dakika ve",kalansaniye,"saniye eder.")
