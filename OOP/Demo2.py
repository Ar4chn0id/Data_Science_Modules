# inheritance(kalıtım) konusu

class Hayvan:
    def __init__(self,deger) -> None:
        print("Hayvan __init__ çağrıldı ")
        self.value = deger

    def method1():
        print("metod 1 çağrıldı")

    def method2():
        print("metod 2 çağrıldı")


class Kedi(Hayvan):
    def __init__(self) -> None:
        print("kedi __init__ çağrıldı")
        super().__init__(deger=12) # kalıtım aldığı sınıfın yapıcı methodunu(__init__) çağırmanın bir yolu (super() kullanılınca init e self konulmaz, hata verir)
        Hayvan.__init__(self,deger=10) # diğer bir yolu
        # bu arada son atanan "deger" kabul görür ama böyle bi kod yazılmaz zaten(iki kere hayvan sınıfının yapıcı methodunun çağrılmasından bahsediyorum)
    
    #override (üstüne yazma) kalıtım aldığı sınıfta da böyle bir fonksiyon var onden üstüne yazma deniyor
    def method2():
        print("miyav")

kedi1 = Kedi()
print(kedi1.value)

print("------------------------------------------------------------")
# Polymorphism
#farklı sınıflardaki aynı ada sahip method ların kullanılmasıdır, açıklayayım:

class sinif1:
    def __init__(self,isim):
        self.isim=isim

    def method(self):
        print(f"{self.isim} in methodu")

class sinif2:
    def __init__(self,isim):
        self.isim=isim

    def method(self):
        print(f"{self.isim} in methodu")

instance1=sinif1("patates")
instance2=sinif2("domates")

listem = [instance1,instance2]

# örnek kullanım 1:

for i in listem:
    print(i.method())


#örnek kullanım 2:

def Bilgi(x):
    return x.method()

Bilgi(instance1)
Bilgi(instance2)


#for döngüsü esnasında none çıktısının sebebini fonksiyonların(method()) bir değer döndürmemesidir, ben sadece print kullandım
#ama Bilgi fonksiyonunda return kullandım. Bu yüzden none yok orada