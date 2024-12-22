import time
z1 = time.time()
with open("d20.1.ornek_metin.txt", "r", encoding="utf-8") as f:
    str_tüm_satırlar = f.read()
    str_tüm_satırlar.replace(" ", "")
    satır_listesi = str_tüm_satırlar.split("\n")
    name_list = []
    puan_listesi = []
    bolum_listesi = []

    for satır in range(len(satır_listesi)):
        name_list.append(satır_listesi[satır].split(" ", 1)[0])
        puan_listesi.append( satır_listesi[satır].rsplit(" ",1)[1] )
        bolum =" ".join(satır_listesi[satır].split(" ")[1:-1])
        bolum_listesi.append(bolum)

name_list.pop(0)
puan_listesi.pop(0)
bolum_listesi.pop(0)
v1_v2_f = []

geçenler = []
kalanlar = []

for i in range(len(name_list)):
    name_list[i] = name_list[i].replace("-"," ")
    v1_v2_f.append( puan_listesi[i].split("/") )
    if int(v1_v2_f[i][0]) * 0.3 + int(v1_v2_f[i][1]) * 0.3 +int(v1_v2_f[i][2]) * 0.4 >= 50 and int(v1_v2_f[i][2]) >= 50 :
        geçenler.append(name_list[i])
        geçenler.append(bolum_listesi[i])
    else:
        kalanlar.append(name_list[i])
        kalanlar.append(bolum_listesi[i])

geçenler_list = []
kalanlar_list = []

for i in range(0, len(geçenler), 2):
    geçenler_list.append(f"{geçenler[i]}  /  {geçenler[i+1]}")

for i in range(0, len(kalanlar), 2):
    kalanlar_list.append(f"{kalanlar[i]}  /  {kalanlar[i+1]}")

with open("d20.1_geçenler.txt", "w", encoding= "utf-8") as f:
    print("KAZANANLAR LİSTESİ")
    f.write("GEÇENLER LİSTESİ\n")
    f.write("--------------------------------------------------------\n")
    for i in range(len(geçenler_list)):
        print(geçenler_list[i])
        f.writelines([geçenler_list[i], "\n"])

with open("d20.1_kalanlar.txt", "w", encoding= "utf-8") as f:
    print("KALANLAR LİSTESİ")
    f.write("KALANLAR LİSTESİ\n")
    f.write("--------------------------------------------------------\n")
    for i in range(len(kalanlar_list)):
        print(kalanlar_list[i])
        f.writelines([kalanlar_list[i], "\n"])

z2= time.time()
print(z2 - z1)