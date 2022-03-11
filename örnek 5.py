saniye=int(input("Saniye:"))
dakika=saniye//60
saat=dakika//60
kalansn=saniye-dakika*60
kalandk=dakika-saat*60
print(saniye," saniye=",saat,"saat",kalandk,"dakika ve",kalansn,"saniye eder")
