kullanici=input("Kullanıcı Adı=")
parola=input("Parola=")

if kullanici=="müdür" and parola=="12345":
    print("Müdür olarak giriş yapıldı")
    
elif kullanici=="öğretmen" and parola=="abcd":
    print("Öğretmen olarak giriş yapıldı")
    
elif kullanici=="öğrenci" and parola=="1a2b3c":
    print("Öğrenci olarak giriş yapıldı")
    
else:
    print("Kullanıcı adı veya parola yanlış")
