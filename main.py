degerler = []
import statistics

if __name__ == '__main__':
    toplama = 0
    while(True):

        secim3 = input("Yeni degerler mi girmek istiyorsunuz var olan bir degeri okumak mi? New or Old")

        while(secim3 == 'New'):

            degerler.append(int(input("Deger giriniz")))
            secim = input("Deger girmeye devam etmek istiyor musunuz? Y or N")

            if(secim == 'Y'):
                continue
            if(secim == 'N'):
                break

        if(secim3 =='Old'):
            try:
                f = open("degerler.txt", "r")
                sayilar = f.read().split(",")
                print(sayilar)
            except FileNotFoundError:
                print("Dosya bulunamadi!")
                continue
        if(secim3 != 'New' and secim3 != 'Old'):
            continue

        while(True):
            secim2 = input("Programdan cikmak mi istiyorsunuz yoksa ortalamanin hesaplanmasini mi? E or A")

            if(secim2 == 'E'):
                quit()
            if(secim2 == 'A'):

                if(secim3 == 'Old'):
                    for x in range(0,len(sayilar)-1):
                        toplama = toplama + int(sayilar[x])

                    median = int((len(sayilar) + 1) / 2)
                    print(toplama)
                    print(f"Mean {(toplama / len(sayilar))}")
                    print(f"Median {sayilar[median-1]}")
                    f.close()
                    break

                if(secim3 == 'New'):
                    print("Mean")
                    print(statistics.mean(degerler))
                    print("Median")
                    print(statistics.median(degerler))
                    f = open("degerler.txt", "w")
                    print(degerler)
                    for x in degerler:
                        f.write(str(x))
                        f.write(",")
                    f.close()
                    break

        break