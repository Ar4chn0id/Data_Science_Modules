#Büyük Veri İşleme: Ödeviniz, büyük bir veri setinde işlem yapmak olacak. 
#İşlem, 100 milyon eleman içeren bir numpy dizisi oluşturacak ve bu dizideki 
#tüm elemanların kareköklerini hesaplayacak. Ardından, bu işlemin ne kadar sürede 
#tamamlandığını ölçmek için zamanlayıcı kullanılacak.

import time as t
import numpy as n
import math


dizi = n.random.randint(0,999999999,100000000) #rastgele elemanlardan oluşan 100.000.000 elemanlı bir numpy dizisi oluşturdum
baslangic=t.thread_time()#süreyi hesaplamak için programın bu noktadaki başlangıç süresini bir değişkende tuttum
for i in dizi: #her bir elemanın karekökünü hesapladım
    math.sqrt(i) # ama bir diziye atmadım
bitis=t.thread_time() # bitiş noktasındaki süreyi de tuttum

print("hesaplama tamamlandı, süre: ",bitis-baslangic) # son olarak bitişten başlangıç süresini çıkardım ve işlem süresini yazdırdım



