class Person(): # class oluştururken baş harfini büyük yazmak önemlidir
    
    göbekadi="Murat" # böyle bir tanımlama person objesi olarak tanımlanan herkesde aynı olacağı anlamına gelir

    def __init__(self,name,age,job="Çiftçi") -> None: # eğer default bir değer tanımlamazsan(name ve age gibi) ve eğer bu class ı çağırdığında da bu değerleri vermezsen hata alırsın.
        print("__init__ çağrıldı")
        self.isim = name #class objesinin adı yerine(Person) self kullanılır. Örnek aşağıda
        self.yas = age
        self.meslek =job
        return None
    
    def ornekfonksiyon(self): #self, fonksiyonun class a ait olduğunu belirtir ve koymak zorunludur
        print(f"Merhaba ben {self.isim}, {self.yas} yaşındayım göbek adım {Person.göbekadi} ve canım kurabiye çekti.") #class a ait özelliklere erişip kullanmak için yine self kullanılır
#                                                        Yukarda "Person" yerine self de kullanılabilir kafa karışmasın

kisi1=Person("Mükremin",20,"Mühendis")
print("-------------------")
print(kisi1.isim, kisi1.yas, "yasında")# class ın özelliğini kullanırken tanımlanan adı, class içinde o özellik için tanımlama yaparken self kullanılır(mesela self.isim)
kisi1.ornekfonksiyon()


