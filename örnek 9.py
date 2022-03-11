girilenSaniye=int(input("Saniye cinsinden zamanı giriniz >"))
kalanSaniye=girilenSaniye%60
dakika=girilenSaniye//60
kalanDakika=dakika%60
saat=dakika//60
print(girilenSaniye,"saniye eşittir,",saat,"saat",kalanDakika,"dakika ve",kalanSaniye,"saniye eder")
