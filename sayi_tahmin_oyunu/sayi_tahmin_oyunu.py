import random                                     #rastgele sayi üretebilmek için random kütüphanesini ekliyoruz

while(True):
    print("sayı tahmin oyununa hos geldiniz".center(50,"*"))
    print("1 ile 100 arasında bir sayı tahmin ediniz".center(50,"*"))
    x=random.randint(1,100)                       #randit() fonksiyonuyla 0 ile 100 arasında rastgele bi sayi üretiyoruz                                       #oyunu kazanma durumunda döngüyü tekrar baslatabilmek icin bi degisken tanımlıyoruz
    can=7 
    while(can>0):                                 #canı her deferinde 1 azaltarak toplamda döngüyü 7 kez tekrarlıyoruz
        try:                                      #int dışında değer girilmesi durumunu kontrol ediyoruz
            tahmin=int(input("Tahmininiz:"))      #kullanıcıdan deger alarak karsılaştırıyoruz
            if(x>tahmin):
                print("yukarı")
            elif(x<tahmin):
                print("asagı")
            else:
                print("tebrikler kazandnız")
                break
            can-=1
        except ValueError:
            print("lütfen bir sayi giriniz")
    if(can==0):                                     #canımızın bitmesi veya oyunu kazanmamız durumunda tekrar oyayıp oynamak istemediğimizi sorguluyoruz
        print("canınız bitti kaybettiniz")
        print("aradıgımız sayi:{}".format(x))
    sor=input("yeniden oynamak ister misiniz(e/h):")
    if(sor=="h"):
        break