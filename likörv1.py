print("""
********************
Legal ve İllegal Kullanıcı Özümseme Rehberi
L.İ.K.Ö.R
v1.5
********************
""")
import sqlite3
import time
con=sqlite3.connect("likör.db") #bağlantı yapar dosya yoksa oluşturur.
cursor=con.cursor()#imleç oluşturduk bu sayede tablo ekleme gibi işlemler yapabiliriz
def tablolustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS Likör(İsim TEXT,Soyisim TEXT,Telefon INT,İlgi TEXT)") #execute (çalıştır) fonksiyonu ile likör tablosu oluşturduk (if not exist yani eğer böyle bir tablo yoksa oluşturacak ) altında datalar oluşturduk ve text ve int olarak belirttik
    con.commit() #databaseye uygulaması için bu komutu kullandık
def veri_ekle():
    try:
        isim=input("İsimi Giriniz\n")
        soyisim=input("Soyismi Giriniz\n")
        telefon=int(input("Telefon Numarasını Giriniz\n"))
        ilgi_alanı=input("İlgi Alanı Giriniz\n")
        cursor.execute("INSERT INTO Likör Values(?,?,?,?)",(isim,soyisim,telefon,ilgi_alanı))
        con.commit()
        print("Veri Ekleme İşlemi Başarılı")
        time.sleep(3)
    except ValueError:
        print("Lütfen telefon numarasını sadece rakamları kullanarak diğer girdileri ise harfleri kullanarak tekrar deneyiniz")
        return veri_ekle()
def isim_veri_cek():
    isim=input("İsim\n")
    cursor.execute("Select * From Likör where İsim=? ",(isim,))
    liste=cursor.fetchall()
    for i in liste:
        print("""
         ---isim----soyisim---telefon-----ilgialanı
        """,i,"""
        --------------------------------------------
        """)
    time.sleep(6)
def soyisim_veri_cek():
    soyisim=input("Soyisim\n")
    cursor.execute("Select * From Likör where Soyisim=? ",(soyisim,))
    liste=cursor.fetchall()
    for i in liste:
        print("""
                 ---isim----soyisim---telefon-----ilgialanı
                """, i, """
                --------------------------------------------
                """)
        time.sleep(6)
def telefon_veri_cek():
    telefon=int(input("Telefon\n"))
    cursor.execute("Select * From Likör where Telefon=? ",(telefon,))
    liste=cursor.fetchall()
    for i in liste:
        print("""
                 ---isim----soyisim---telefon-----ilgialanı
                """, i, """
                --------------------------------------------
                """)
        time.sleep(6)
def ilgi_veri_cek():
    ilgi=input("İlgi Alanı\n")
    cursor.execute("Select * From Likör where İlgi=? ",(ilgi,))
    liste=cursor.fetchall()
    for i in liste:
        print("""
                 ---isim----soyisim---telefon-----ilgialanı
                """, i, """
                --------------------------------------------
                """)
        time.sleep(6)
class guncelle():
    def isim():
        eski_ad=input("Kişinin önceki ismini girin.")
        yeni_ad=input("Kişinin yeni ismini girin.")
        cursor.execute("Update Likör set İsim=? where İsim=?",(yeni_ad,eski_ad))
        con.commit()
        print("İsim Güncelleme Başarılı")
        time.sleep(3)
    def soyisim():
        eski_soyisim=input("Kişinin önceki soyismini girin")
        yeni_soyisim=input("Kişinin yeni soyismini girin")
        cursor.execute("Update Likör set Soyisim=? where Soyisim=?",(yeni_soyisim,eski_soyisim))
        con.commit()
        print("Soyisim Güncelleme Başarılı")
        time.sleep(3)
    def telefon():
        try:
            eski_telefon=int(input("Kişinin eski telefon numarasını girin."))
            yeni_telefon=int(input("Kişinin yeni telefon numarasını girin."))
            cursor.execute("Update Likör set Telefon=? where Telefon=?",(yeni_telefon,eski_telefon))
            con.commit()
            print("Telefon Güncelleme Başarılı")
            time.sleep(3)
        except ValueError:
            print("Sadece Rakamları Kullanın")
    def ilgi_alani():
        eski_ilgi_alani=input("Kişinin eski ilgi alanını giriniz.")
        yeni_ilgi_alani=input("Kişinin yeni ilgi alanını giriniz.")
        cursor.execute("Update Likör set İlgi=? where İlgi=?",(yeni_ilgi_alani,eski_ilgi_alani))
        con.commit()
        time.sleep(3)
        print("İlgi Alanı Güncelleme Başarılı")
while True:
    islem=input("""
********************
Legal ve İllegal Kullanıcı Özümseme Rehberi
L.İ.K.Ö.R
***
*Veri Tabanına Bilgi Girişi İçin 1 Tuşuna Bas
**Veri Tabanından Bilgi Düzenleme İçin 2 Tuşuna Bas
***Veri Tabanından Bilgi Çekmek İçin 3 Tuşuna Bas 
********************
yapmak istediğin işlemin numarasını gir çıkmak için 'q' tuşuna bas.\n     
    """)
    if (islem=="q"):
        print("Uygulama Kapatılıyor...")
        con.close()
        time.sleep(3)
        break
    islem=int(islem)
    if(islem==1):
        print("Veri Ekleme Başlatılıyor...")
        time.sleep(3)
        veri_ekle()
    elif(islem==2):
        print("""
        **********
        İsim güncellemek için 1
        Soyisim güncellemek için 2
        Telefon güncellemek için 3
        İlgi alanı güncellemek için 4
        **********
        """)
        time.sleep(2)
        try:
            giris = input("Lütfen yapmak istediğiniz işlemi giriniz.")
            giris=int(giris)
            if(giris==1):
                guncelle.isim()
            elif(giris==2):
                guncelle.soyisim()
            elif(giris==3):
                guncelle.telefon()
            elif(giris==4):
                guncelle.ilgi_alani()
        except ValueError:
            print("Sadece Rakamları Kullan")
    elif(islem==999):
        tablolustur()
    elif(islem==3):
        print("Veri Çekme Başlatılıyor...")
        time.sleep(3)
        print("""
        ********************
        İsime göre aramak için 1
        Soyisime göre aramak için 2
        Telefon numarasına göre aramak için 3
        İlgi Alanına göre aramak için 4 
        rakamlarını kullanın
        *********************
        """)
        tercih=int(input("Lütfen yapmak istediğiniz işlemi girin"))
        try:
            if(tercih==1):
                isim_veri_cek()
            elif(tercih==2):
                soyisim_veri_cek()
            elif(tercih==3):
                telefon_veri_cek()
            elif(tercih==4):
                ilgi_veri_cek()
            else:
                print("Böyle bir işlem yok")
                break
        except ValueError:
            print("Sadece Rakamları Kullan")
            break