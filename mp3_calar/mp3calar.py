import random

class Mp3calar():
    ses=20
    
    
    def __init__(self,sarkılar=["tarkan","hadise","manga"]):
        self.sarkılar=sarkılar
        self.sarkı=random.choices(self.sarkılar)
    
    
    def menu(self):
        print("sarkı listesi={}".format(self.sarkılar))
        print("su an calan sarkı={}".format(self.sarkı))
        print("""
    1.)Sarkı sec
    2.)Ses Arttır
    3.)Ses Azalt
    4.)Rastgele sarkı sec
    5.)Sarkı ekle
    6.)Sarkı sil
    7.)Kapat
    """)
        return int(input("lütfen yapmak istediginiz islemi secin:"))
                    
    def sarkı_sec(self):
        sec=input("secmek istediginiz sarkı nedir:")
        if sec not in self.sarkılar:
            print("bu sarkı bulunmuyor")
        else:
            print("{} secildi\n".format(sec))
            self.sarkı=sec
    def sesArttir(self):
        self.ses+=2
        print("ses düzeyi:{}\n".format(self.ses))
    
    def sesAzalt(self):
        self.ses-=2
        print("ses düzeyi:{}\n".format(self.ses))
    
    def rastgeleSarkısec(self):
        x=random.randint(0,len(self.sarkılar)-1)
        print("rastgele secilen sarkı={}".format(self.sarkılar[x]))
        self.sarkı=self.sarkılar[x]
        print("")
    
    def sarkıEkle(self):
        yeni=input("eklemek istediginiz sarkı nedir:")
        self.sarkılar.append(yeni)
        print("yeni sarkı eklendi\n")
    
    def sarkıSil(self):
        sil=input("silmek istediginiz sarki adı:")
        if sil not in self.sarkılar:
            print("bu sarkı zaten listede bulunmamakta")
        else:
            self.sarkılar.remove(sil)
            print("sarki silindi")
    
    def calıstır(self):
        while(True):
            try:
                x=self.menu()
                while(x<1 or x>7):
                    print("lütfen 1 ile 7 arasında sayi giriniz")
                    print("\n\n")
                    x=self.menu()
                    
                if(x==1):
                    self.sarkı_sec()
                elif(x==2):
                    self.sesArttir()
                elif(x==3):
                    self.sesAzalt()
                elif(x==4):
                    self.rastgeleSarkısec()
                elif(x==5):
                    self.sarkıEkle()
                elif(x==6):
                    self.sarkıSil()
                else:
                    break
            except ValueError:
                print("lütfen bir sayı giriniz")


mp3=Mp3calar()
mp3.calıstır()


        
    
