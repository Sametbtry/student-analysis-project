import time
z1 = time.time()
with open("d20.1.ornek_metin.txt", "r", encoding="utf-8") as f:
    str_tüm_satırlar = f.read()
    satır_listesi = str_tüm_satırlar.split("\n")
    baslık = satır_listesi.pop(0)
    print(baslık)

with open("d20.1_geçenler.txt", "w", encoding="utf-8") as g:
    with open("d20.1_kalanlar.txt", "w", encoding="utf-8") as k:
        g.writelines(["name", (25 - len("name")) * " "])
        g.writelines(["surname", (25 - len("surname")) * " "])
        g.writelines(["bölum", (25 - len("bölüm")) * " "])
        g.writelines(["not ortalaması", (25 - len("not ortalaması")) * " "])
        g.writelines(["durum", (25 - len("durum")) * " ", "\n"])
        g.writelines(5 * ["-----------", (25 - len("-----------")) * " "])
        g.write("\n")

        k.writelines(["name", (25 - len("name")) * " "])
        k.writelines(["surname", (25 - len("surname")) * " "])
        k.writelines(["bölum", (25 - len("bölüm")) * " "])
        k.writelines(["not ortalaması", (25 - len("not ortalaması")) * " "])
        k.writelines(["durum", (25 - len("durum")) * " ", "\n"])
        k.writelines(5 * ["-----------", (25 - len("-----------")) * " "])
        k.write("\n")


        for satır in satır_listesi:
            print() #boşluk
            print(satır)
            ad_soyad = satır.split(" ")[0]
            soyad = ad_soyad.split("-")[-1]
            ad = ad_soyad[0: ad_soyad.index(soyad)].replace("-", " ")
            print(ad)
            print(soyad)

            bolum = satır.split(" ")[1:-1]
            bolum = " ".join(bolum)
            print(bolum)

            v1_v2_f = satır.split(" ")[-1]
            v1_v2_f = v1_v2_f.split("/")
            v1 = int(v1_v2_f[0])
            v2 = int(v1_v2_f[1])
            f = int(v1_v2_f[2])
            print(v1, v2 , f)
            ort = round((( v1 + v2 ) * 0.3 + f * 0.4), 2)

            if ( v1 + v2 ) * 0.3 + f * 0.4 >= 70 and f >= 70 :
                g.writelines([ad, (25 - len(ad)) * " "])
                g.writelines([soyad, (25 - len(soyad)) * " "])
                g.writelines([bolum, (25 - len(bolum)) * " "])
                g.writelines([str(ort), 20 * " "])
                g.writelines(["geçti", (25 - len("geçti")) * " ", "\n"])
            else:
                k.writelines([ad, (25 - len(ad)) * " "])
                k.writelines([soyad, (25 - len(soyad)) * " "])
                k.writelines([bolum, (25 - len(bolum)) * " "])
                k.writelines([str(ort), 20 * " "])
                k.writelines(["kaldı", (25 - len("kaldı")) * " ", "\n"])

z2 = time.time()
print(z2 - z1)

#programın sürekli açık kalması için
input("Program tamamlandı. Kapatmak enter tuşuna basınız.")

