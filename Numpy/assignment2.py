#Sinüs Dalgası İşleme: Ödeviniz, numpy kütüphanesi kullanarak sinüs dalga işleme yapmak olacak. 
#İşlem, 2π aralığında 1000 örnekle örneklenecek ve ardından örneklerdeki her 20. örneği alınacak.
# Alınan örnekler daha sonra her biri 2π içindeki aralığında karekök alınarak işlenecek ve son olarak
# işlenen verilerin ortalaması hesaplanacak.

import numpy as np

# 2π aralığında 1000 örnekle örnekleme yaptım
t = np.linspace(0, 2*np.pi, 1000)

# Örneklerdeki her 20. örneği aldım
t = t[::20]

# Alınan örnekleri karekök alarak işledim
result = np.sqrt(t)

# İşlenen verilerin ortalamasını hesapladım
mean = np.mean(result)

print(mean)