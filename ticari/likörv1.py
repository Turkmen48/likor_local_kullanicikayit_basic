print("""
********************
Enes Kırtasiye Kitap Kayıt Sistemi
**Made by Turkmensoft**
********************
""")
import sqlite3
import time
con=sqlite3.connect("likör.db") #bağlantı yapar dosya yoksa oluşturur.
cursor=con.cursor()#imleç oluşturduk bu sayede tablo ekleme gibi işlemler yapabiliriz
def tablolustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS eneskırtasiye(İsim TEXT,Yayın TEXT,Sayfa INT,Fiyat TEXT)") #execute (çalıştır) fonksiyonu ile likör tablosu oluşturduk (if not exist yani eğer böyle bir tablo yoksa oluşturacak ) altında datalar oluşturduk ve text ve int olarak belirttik
    con.commit() #databaseye uygulaması için bu komutu kullandık
def veri_ekle():
    try:
        isim=input("Kitap İsimi Giriniz\n")
        soyisim=input("Kitabın Yayın evini giriniz\n")
        telefon=int(input("Kitabın sayfa sayısını giriniz\n"))
        ilgi_alanı=input("Kitabın fiyatını giriniz\n")
        cursor.execute("INSERT INTO eneskırtasiye Values(?,?,?,?)",(isim,soyisim,telefon,ilgi_alanı))
        con.commit()
        print("Veri Ekleme İşlemi Başarılı")
        time.sleep(3)
    except ValueError:
        print("Lütfen telefon numarasını sadece rakamları kullanarak diğer girdileri ise harfleri kullanarak tekrar deneyiniz")
        return veri_ekle()
def isim_veri_cek():
    isim=input("İsim\n")
    cursor.execute("Select * From eneskırtasiye where İsim=? ",(isim,))
    liste=cursor.fetchall()
    for i in liste:
        print(i)
    time.sleep(3)
def soyisim_veri_cek():
    soyisim=input("Yayınevi\n")
    cursor.execute("Select * From eneskırtasiye where Yayın=? ",(soyisim,))
    liste=cursor.fetchall()
    for i in liste:
        print(i)
    time.sleep(3)
def telefon_veri_cek():
    telefon=int(input("Sayfa sayısı\n"))
    cursor.execute("Select * From eneskırtasiye where Sayfa=? ",(telefon,))
    liste=cursor.fetchall()
    for i in liste:
        print(i)
    time.sleep(3)
def ilgi_veri_cek():
    ilgi=input("Fiyat\n")
    cursor.execute("Select * From eneskırtasiye where Fiyat=? ",(ilgi,))
    liste=cursor.fetchall()
    for i in liste:
        print(i)
    time.sleep(3)
class guncelle():
    def isim():
        eski_ad=input("Kitabın önceki ismini girin.")
        yeni_ad=input("Kitabın yeni ismini girin.")
        cursor.execute("Update eneskırtasiye set İsim=? where İsim=?",(yeni_ad,eski_ad))
        con.commit()
        print("İsim Güncelleme Başarılı")
        time.sleep(3)
    def soyisim():
        eski_soyisim=input("Kitabın önceki yayınevini girin")
        yeni_soyisim=input("Kitabın yeni yayınevini girin")
        cursor.execute("Update eneskırtasiye set Yayın=? where Yayın=?",(yeni_soyisim,eski_soyisim))
        con.commit()
        print("Yayın Güncelleme Başarılı")
        time.sleep(3)
    def telefon():
        try:
            eski_telefon=int(input("Kitabın eski sayfa sayısını numarasını girin."))
            yeni_telefon=int(input("Kitabın yeni sayfa sayısını girin."))
            cursor.execute("Update eneskırtasiye set Sayfa=? where Sayfa=?",(yeni_telefon,eski_telefon))
            con.commit()
            print("Sayfa sayısı Güncelleme Başarılı")
            time.sleep(3)
        except ValueError:
            print("Sadece Rakamları Kullanın")
    def ilgi_alani():
        eski_ilgi_alani=input("Kitabın eski fiyatını alanını giriniz.")
        yeni_ilgi_alani=input("Kitabın yeni fiyatını giriniz.")
        cursor.execute("Update eneskırtasiye set Fiyat=? where Fiyat=?",(yeni_ilgi_alani,eski_ilgi_alani))
        con.commit()
        time.sleep(3)
        print("Fiyat Güncelleme Başarılı")
while True:
    islem=input("""
********************
Enes kırtasiye kitap kayıt sistemi
**Made by Turkmensoft**
***
*Kitap Girişi İçin 1 Tuşuna Bas
**Kitap Düzenleme İçin 2 Tuşuna Bas
***Kitap Çekmek İçin 3 Tuşuna Bas 
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
        Yayın güncellemek için 2
        Sayfa sayısı güncellemek için 3
        Fiyat güncellemek için 4
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
        Yayına göre aramak için 2
        Sayfa sayısına numarasına göre aramak için 3
        Fiyata göre aramak için 4 
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