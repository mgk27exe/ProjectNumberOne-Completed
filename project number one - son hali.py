import sqlite3 as sql
islem = """
(1)Amiral battı oyunu
(2)Hesap Makinası
(3)İletişim
(4)Çıkış
"""

print(islem)
isimi = input("Lutfen isminizi giriniz: ")
def veritabani(isim, islemi):
    vt = sql.connect("Kullanicilar.db")
    im = vt.cursor()
    olustur = """CREATE TABLE IF NOT EXISTS Kullanicilar (isimler,islemler)"""
    ekle = """INSERT INTO Kullanicilar VALUES (?,?)"""
    im.execute(olustur)
    im.execute(ekle,(isim,islemi))
    vt.commit()
    vt.close()
while True:
    islem = input("Yapmak istediğiniz işlemin numarasını seçiniz: \n[Çıkmak için 4. seçeneği seçiniz]\n")
    if islem == "4":
        print("Çıkış Yapılıyor...")
        break
    elif islem == "3":
        print("Hakkımızda bölümüne yönlendiriliyorsunuz...")
        print("""
              instagram: https://www.instagram.com/mgorkemklc/
              github: https://github.com/mgk27exe
              linkedin: https://www.linkedin.com/in/m-g-k-197524211/
              youtube: https://www.youtube.com/channel/UCqa4-8vB3GQD7cuVN7DOBBw
              spotify: https://open.spotify.com/user/e5afmyz44tqikxp3w7hzsb14w
              NFT satış: https://opensea.io/Saint_Alcala
              steam: https://steamcommunity.com/id/mgking27/
              """)
    elif islem == "2":
        print("Hesap Makinesi Açılıyor...\n")

        while True:

            def toplama(a, b):
                return a + b


            def cikarma(a, b):
                return a - b


            def carpma(a, b):
                return a * b


            def bolme(a, b):
                return a / b


            print("Bir işlem seçiniz...")
            print("Toplama işlemi için 1'e basınız.")
            print("Çıkarma işlemi için 2'ye basınız.")
            print("Çarpma işlemi için 3'e basınız.")
            print("Bölme işlemi için 4'e basınız.")

            secim = input("Hangi işlemi yapmak istersiniz (1 - 2 - 3 - 4):")

            sayi1 = int(input("Birinci sayıyı giriniz = "))
            sayi2 = int(input("İkinci sayıyı giriniz = "))

            if secim == '1':
                print(sayi1, "+", sayi2, "=", toplama(sayi1, sayi2))

            elif secim == '2':
                print(sayi1, "-", sayi2, "=", cikarma(sayi1, sayi2))

            elif secim == '3':
                print(sayi1, "*", sayi2, "=", carpma(sayi1, sayi2))

            elif secim == '4':
                print(sayi1, "/", sayi2, "=", bolme(sayi1, sayi2))
            else:
                print("Değer girilmedi.")

            tercih = input("Başka işlem yapmak istiyor musunuz ? (E/H) \n")
            if tercih == 'E':
                break

    elif islem == "1":
        print("Amiral battı oyunu açılıyor...")

        from random import randint

        board = []
        sayac = 0
        puan = 250
        for i in range(5):
            board.append(["0"] * 5)


        def print_board(board):
            for satir in board:
                print(" ".join(satir))


        def rand(board):
            return randint(1, len(board) - 1)


        print("-" * 35)
        print("Amiral batti oyununa hosgeldiniz! -Oyun yapimcisi M.Gorkem Kilic ")
        print("-" * 35)
        print("PuanÄ±nÄ±z:", puan)
        print("-" * 35)
        print_board(board)

        gemi_satir = rand(board)
        gemi_sutun = rand(board)
        gemi1_satir = rand(board)
        gemi1_sutun = rand(board)
        gemi2_satir = rand(board)
        gemi2_sutun = rand(board)

        while True:
            if (gemi_satir == gemi1_satir and gemi_sutun == gemi1_sutun):
                gemi1_satir = rand(board)
                gemi1_sutun = rand(board)
                continue
            elif (gemi_satir == gemi2_satir and gemi_sutun == gemi2_sutun):
                gemi2_satir = rand(board)
                gemi2_sutun = rand(board)
                continue
            elif (gemi1_satir == gemi2_satir and gemi1_sutun == gemi2_sutun):
                gemi2_satir = rand(board)
                gemi2_sutun = rand(board)
                continue
            else:
                print("-" * 35)
                tahmin_satir = int(input("SatÄ±r giriniz: "))
                tahmin_sutun = int(input("SÃ¼tun giriniz: "))
                tercih = input("Başka işlem yapmak istiyor musunuz ? (E/H) \n")
                if tercih == 'E':
                    break
                if (tahmin_satir == gemi_satir and tahmin_sutun == gemi_sutun) \
                        or (tahmin_satir == gemi1_satir and tahmin_sutun == gemi1_sutun) \
                        or (tahmin_satir == gemi2_satir and tahmin_sutun == gemi2_sutun):
                    if board[tahmin_satir - 1][tahmin_sutun - 1] == "/":
                        print("-" * 35)
                        print("Zaten tahmin ettiniz")
                        print_board(board)
                        print(puan)
                    else:
                        print("-" * 35)
                        print("Tebrikler gemiyi batirdiniz!")
                        board[tahmin_satir - 1][tahmin_sutun - 1] = "/"
                        print("Puaniniz:", puan)
                        print("-" * 35)
                        print_board(board)
                        sayac += 1
                else:
                    if (tahmin_satir < 0 or tahmin_sutun < 0) or (tahmin_satir > 5 or tahmin_sutun > 5):
                        print("-" * 35)
                        print("Alan sÄ±nÄ±rlarÄ± dÄ±ÅÄ±nda deÄer girdiniz")

                    elif board[tahmin_satir - 1][tahmin_sutun - 1] == "X":
                        print("-" * 35)
                        print("Zaten tahmin ettiniz")
                        print("-" * 35)
                        print_board(board)
                    else:
                        print("-" * 35)
                        print("VuramadÄ±nÄ±z")
                        board[tahmin_satir - 1][tahmin_sutun - 1] = "X"
                        puan -= 10
                        print("PuanÄ±nÄ±z:", puan)
                        print("-" * 35)
                        print_board(board)

                    if sayac == 3:
                        print("-" * 35)
                        print("Tebrikler bÃ¼tÃ¼n gemileri batÄ±rdÄ±nÄ±z ve oyunu kazandÄ±nÄ±z")
                        print("-" * 35)
                        break
    else:
        print("LÜTFEN GEÇERLİ İŞLEM NUMARASI GİRİNİZ...")
veritabani(isimi,islem)