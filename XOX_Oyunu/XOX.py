class Oyun():
    
    def __init__(self):
        self.tahta=[["#","#","#"],["#","#","#"],["#","#","#"]]
        self.sıra=0
        self.check=True
    
    def ekrana_yazdir(self):
        i=1
        print("  1 2 3 ")
        for satir in self.tahta:
            print(i,end=" ")
            for sutun in satir:
                print(sutun,end=" ")
            print("")
            i+=1
    
    def hamle(self):
        try:
            a="O"
            if self.sıra%2==0:a="X"
            print("{}.OYUNCU({})".format(self.sıra%2+1,a),end="")
            x=int(input("satır sayısını giriniz:"))-1
            y=int(input("sutun sayisini giriniz:"))-1
            while(x<0 or x>2 or y<0 or y>2):
                print("lütfen satir ve sutun 1 ile 3 arasında olacak sekilde secim yapın \n")
                print("{}.OYUNCU".format(self.sıra%2+1),end="")
                x=int(input("satır sayısını giriniz:"))-1
                y=int(input("sutun sayisini giriniz:"))-1
                
            print("")       
            self.isle(x,y)
        except ValueError:
            print("Lütfen sadece tam sayı giriniz:\n".upper())
            self.hamle()
        
    def isle(self,x,y):     
        if(self.tahta[x][y]!="#"):
            print("lütfen baska alan seciniz \n")
            self.hamle()
        else:
            if(self.sıra%2==0):
                self.tahta[x][y]="X"
            else:
                self.tahta[x][y]="O"
            self.ekrana_yazdir()
            self.sıra+=1
    def kontrol(self):
        for i in range(2):
            if(self.tahta[i][0]==self.tahta[i][1]==self.tahta[i][2]!="#"):
                return False
            elif(self.tahta[0][i]==self.tahta[1][i]==self.tahta[2][i]!="#"):
                return False
            elif(self.tahta[0][0]==self.tahta[1][1]==self.tahta[2][2]!="#"):
                return False
            elif(self.tahta[0][2]==self.tahta[1][1]==self.tahta[2][0]!="#"):
                return False
        return True
    
    def calıstır(self):
        self.ekrana_yazdir()
        while(self.check):
            self.hamle()
            self.check=self.kontrol()
            if(not self.check):
                if self.sıra%2==1:
                    print("oyun bitti X kazandı")
                else:
                    print("oyun bitti O kazandı")
        
oyun=Oyun()
oyun.calıstır()
        