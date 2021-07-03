import sqlite3
con=sqlite3.connect("likördeneme.db") #bağlantı yapar dosya yoksa oluşturur.
cursor=con.cursor()#imleç oluşturduk bu sayede tablo ekleme gibi işlemler yapabiliriz
def tablolustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS Likör(İsim TEXT,Soyisim TEXT,Telefon Numarası INT,İlgialani TEXT)") #execute (çalıştır) fonksiyonu ile likör tablosu oluşturduk (if not exist yani eğer böyle bir tablo yoksa oluşturacak ) altında datalar oluşturduk ve text ve int olarak belirttik
    con.commit() #databaseye uygulaması için bu komutu kullandık
def veri_ekle():
    cursor.execute("insert into Likör Values('ENES','durmuş','5061793786','fitness')") #sql kodları büyük küçüük yazmak bir şeyi değiştirmez ama genelde büyük yazılır. Burada da insert into Tablo_adı Values('birinci değer','ikinci değer') şeklinde girilir.
    con.commit()
#tablolustur()
#veri_ekle()
#con.close()#databaseyi kapattık
def veri_ekle2(isim,soyisim,telefon,ilgi_alani):
    cursor.execute("INSERT INTO Likör Values(?,?,?,?)",(isim,soyisim,telefon,ilgi_alani)) #? lerin yerine verdiğimiz değişkenler geçecek
    con.commit()

isim=input("isim")
soyisim=input("soyisim")
telefon=input("telefon")
ilgi_alani=input("ilgi alani")
veri_ekle2(isim,soyisim,telefon,ilgi_alani)
con.close()
#Select*From Likör likör tablosundaki her şeyi çeker.
#Selct İsim,Soyisim From Likör likör tablosundan isim ve soyisimi çekiyor
#Select*From Likör where İsim="enes" ismi enes olanların bilgilerini getiriyor.
def verileri_cek():
    cursor.execute("Select*From Likör")
    liste=cursor.fetchall()#cursor.fetchall ile verilerin bize dönmesini sağlıyoruz ve bu dönen verileri liste değişkenine kaydediyoruz
    #con.commit() kullanmaya gerek yok çünkü veritabanına bir şey uygulamıyoruz sadece okuyoruz yazmıyoruz.
    for i in liste:
        print(liste)
def verileri_cek2():
    cursor.execute("Select İsim,Soyisim From Likör")
    liste=cursor.fetchall()
    for i in liste:
        print(liste)
def verileri_cek3(isim):
    cursor.execute("Select * From Likör where isim=?",(isim))
    liste=cursor.fetchall()
    for i in liste:
        print(i)
def verileri_guncelle():
    cursor.execute("Update Likör set İsim=? where=? ",(yeni_isim,eski_isim))