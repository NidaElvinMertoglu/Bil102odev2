class Magaza:
    def __init__(self, magaza_adi, satici_adi, satici_cinsi):
        self.__magaza_adi = magaza_adi
        self.__satici_adi = satici_adi
        self.__satici_cinsi = satici_cinsi
        self.__satislar = {}

    def magaza_satis_tutari(self):
        toplam_satis_tutari = 0
        for satis_tarihi, tutar in self.__satislar.items():
            toplam_satis_tutari += tutar
        return toplam_satis_tutari

    def satici_satis_tutari(self):
        toplam_satis_tutari = 0
        for satis_tarihi, tutar in self.__satislar.items():

                toplam_satis_tutari += tutar
        return toplam_satis_tutari

    def satis_kaydet(self, satis_tarihi, tutar):
        self.__satislar[satis_tarihi] = tutar

    def get_magaza_adi(self):
        return self.__magaza_adi

    def set_magaza_adi(self, magaza_adi):
        self.__magaza_adi = magaza_adi

    def get_satici_adi(self):
        return self.__satici_adi

    def set_satici_adi(self, satici_adi):
        self.__satici_adi = satici_adi

    def get_satici_cinsi(self):
        return self.__satici_cinsi

    def set_satici_cinsi(self, satici_cinsi):
        self.__satici_cinsi = satici_cinsi

def main():
    magazalar = {}
    while True:
        magaza_adi = input("Magaza adini giriniz: ")
        satici_adi = input("Satici adini giriniz: ")
        satici_cinsi = input("Satilan urunun ne oldugunu giriniz: ")
        satis_tarihi = input("Satis tarihini (gun.ay.yil) olaraktan giriniz: ")
        tutar = float(input("Satis tutarini giriniz: "))


        if magaza_adi not in magazalar:
            magazalar[magaza_adi] = Magaza(magaza_adi, satici_adi, satici_cinsi)

        magazalar[magaza_adi].satis_kaydet(satis_tarihi, tutar)

        devam = input("Yeni satis eklemek istiyor musunuz? (e/h): ")
        if devam.lower() != "e":
            break

    for magaza_adi, magaza in magazalar.items():
        print(f"{magaza_adi}:")
        print(f"\t{magaza.get_satici_adi()} isimli saticinin satis tutari: {magaza.satici_satis_tutari()}")
        print(f"\tToplam satis tutari: {magaza.magaza_satis_tutari()}")



if __name__ == "__main__":
    main()
