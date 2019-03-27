import sqlite3
class Kutuphane():

    def __init__(self):

        self.veritabanı = sqlite3.connect("kutuphane.sqlite")
        self.imleç = self.veritabanı.cursor()
        self.imleç.execute("CREATE TABLE IF NOT EXISTS Kitap(KitapAdi TEXT, YazarAdi TEXT, BasimYili INTEGER)")
        self.ana_menü()

    def ana_menü(self):

        self.ana_menü = "[1] Tabloya Kayıt Ekleme\n" \
                   "[2] Tüm Kayıtları Listele\n" \
                   "[3] Var Olan Kaydı Güncelleme\n" \
                   "[4] Kayıt Silme\n" \
                   "[0] Çıkış"
        print(self.ana_menü)
        print()

        while True:
            self.seçim = input("Seçiminiz --> ")
            print()

            if self.seçim == "1":
                self.ekle()

            elif self.seçim == "2":
                self.listele()

            elif self.seçim == "0":
                import time
                print("Program kapanıyor...")
                time.sleep(3)
                raise SystemExit

    def ekle(self):

        self.veritabanı = sqlite3.connect("kutuphane.sqlite")
        self.imleç = self.veritabanı.cursor()
        kitap_adı = input("Kitap Adı  : ")
        yazar_adı = input("Yazar Adı  : ")
        basım_yılı = int(input("Basım Yılı : "))

        kitaplar = []
        kitaplar.append((kitap_adı, yazar_adı, basım_yılı))

        for veri in kitaplar:
            self.imleç.execute("INSERT INTO Kitap VALUES (?,?,?)", veri)

        self.veritabanı.commit()
        self.veritabanı.close()
        print("Kayıt Eklendi !")
        print()

    def listele(self):
        self.veritabanı = sqlite3.connect("kutuphane.sqlite")
        self.imleç = self.veritabanı.cursor()
        satır = " Kitap Adı               Yazar Adı              Basım Yılı"
        # print(len(satır))
        print(satır)
        print()

        self.imleç.execute("SELECT * FROM Kitap ORDER BY KitapAdi")
        sonuç = self.imleç.fetchall()
        for s in sonuç:
            boşluk1 = 23 - len(s[0])
            boşluk2 = 23 - len(s[1])
            # boşluk3 = 23 - len(str(s[2]))

            print(" " + s[0] + boşluk1 * " " + " " + s[1] + boşluk2 * " " + str(s[2]))
            # print(58*"-")

        self.veritabanı.close()
        print()

ktb = Kutuphane()
