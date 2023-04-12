# class yapısında özel methodlar
class Meyve:
    def __init__(self,tür,kalori) -> None: # bu özel metodun ne işe yaradığını biliyoruz
        self.type=tür
        self.cal = kalori

    def __str__(self) -> str: # bu özel metod sınıf objesi mesela print edilirse ne çıktı verileceğini belirtir. Örnek aşağıda verilecek
        return f"bu bir meyvedir ve türü:{self.type}, kalorisi: {self.cal}"
    
    def __len__(self) -> int: # mesela len diye de bir özel metod var bu ise len() fonksiyonunda değer döndürmesini sağlar. bu örnek için pek uygun değil ama mantığını kavramak için idare eder
        return self.cal



uzum=Meyve("üzüm",100)

print(uzum)# __str__ için örnek kullanım

print("üzümün boyutu :D ",len(uzum),"kalori") # __str__ için örnek kullanım