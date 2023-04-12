#Büyük Dizilerde Sıralama: Ödeviniz, numpy kütüphanesi kullanarak büyük bir dizi içindeki elemanları sıralamak olacak. 
#İşlem, 1 milyar eleman içeren bir numpy dizisi içindeki elemanları rastgele seçecek ve bu elemanları sıralayacak. 
#Ardından, bu işlemin ne kadar sürede tamamlandığını ölçmek için zamanlayıcı kullanılacak.

import numpy as n
import time
dizim=n.random.randint(0,1000000000,1000000000)
basla=time.thread_time()
dizim.sort()
bitir=time.thread_time()
print("geçen süre: ",bitir-basla)



