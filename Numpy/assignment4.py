#Son ödeviniz, numpy kütüphanesi kullanarak istatistiksel işlemler yapmak olacak. 
#İşlem, bir veri seti içindeki elemanların standart sapmasını, varyansını ve ortalamasını hesaplayacak. 
#Veri seti, numpy kütüphanesinde bulunan random.normal fonksiyonu kullanılarak rastgele oluşturulacak ve 
#1 milyon eleman içerecek.

import numpy as n

dataset=n.random.normal(size=1000000) # random.normal ile 1 milyon boyutunda dizi oluşturdum
print(dataset)

standartsapma = n.std(dataset) # standart sapma, varyans ve ortalamayı numpy kütüphanesindeki fonksiyonları kullanarak buldum
varyans= n.var(dataset)
ortalama=n.mean(dataset)
#ve yazdırdım
print(f"""\nDataset Bilgileri: 

Standart sapma: {standartsapma}
Varyans: {varyans}
Ortalama: {ortalama}
""")


