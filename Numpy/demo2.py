# dizi metodları

import numpy as n
myarray=n.random.randint(0,20,12)
print(myarray)

print(myarray.max()) # dizideki max değeri döndürür
print(myarray.min())# dizideki min değeri döndürür
print(myarray.argmax())# dizideki max değerin indexini döndürür
print(myarray.mean())# dizideki değerlerin ortalamasını döndürür
print(myarray.shape)# dizinin boyut şeklini döndürür değeri döndürür(kaça kaç olduğunu)
print(myarray.reshape(3,4))# diziyi yeniden boyutlandırır(dizideki eleman sayısına göre yaptığı için 6 elemanlı bir diziyi 10x5 şeklinde reshape yapamazsın)
newarray = myarray.reshape(3,4)
print("transpoz işlemi: \n",newarray.transpose())# dizinin transpozunu alır


print("--------------------------------------------------------------")

#slicing
yeni=n.arange(10,30)
print(yeni[3:10])# numpy dizilerinde de slicing aynı mantıkta çalışır ANCAK
slicem = yeni[3:10] # yeni dizisinin bir parçasını başka bir değişkene atıyorum
slicem[:] = 1000 # ve o dizinin bütün elemanlarını değiştiriyorum
print(slicem) # normal olarak slicem dizisi değişti
print(yeni) # ama parça aldığım ana dizinin de alınan parçası değişti.
# buna engel olmak için copy() kullanılır

yepyeni = n.arange(10,30)
print(yepyeni)
yepisyeni = yepyeni.copy()[3:10] # burada oluşturulan yepisyeni diziyi kopya parça olarak tanımladık
print(yepisyeni)
yepisyeni[:] = 2222 
print(yepisyeni) #sonuç olarak yepisyeninin elemanlarında değişiklik yaptığımda
print(yepyeni) # yepyeni dizim değişmemiş oldu  
print("--------------------------------------------------------------")
#matrikslerde slicing...
yenimatriks = n.arange(10,30).reshape(5,4)
print(yenimatriks)

print(yenimatriks[[0,2,4]]) #belirli satırları seçmek için [[]] kullanılır

#slicing işlemi

print(yenimatriks[1:,1:3]) # ilki satır indexleri ile ikincisi sütun indexleri ile ilgili (1 indexli sütundan sonuna kadar ve 1 indexli sütundan 3 indexli sütuna kadar(3 dahil değil))

print("--------------------------------------------------------------")
#matrikslerde matematiksel operasyonlar

newmatrix=n.random.randint(20,40,20)

print(newmatrix < 25)
sonuc=newmatrix < 25
sonucdizisi=newmatrix[sonuc]
print(sonucdizisi)

print(newmatrix+newmatrix)
print(newmatrix-newmatrix)
print(newmatrix*newmatrix)
print(newmatrix/newmatrix)