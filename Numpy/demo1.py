import numpy as n

#listeleri numpy array e çevirme işlemi

mylist=[1,2,34,5,6,67,5]
print(type(mylist))
my_numpy_list=n.array(mylist)
print(type(my_numpy_list))

mylist2 =[[1,23,4,5],[12,1,323,43],[12,456,6343,4]]
print(mylist2[1][3])
my_numpy_list2= n.array(mylist2)

print(my_numpy_list2)

print("-------------------------------------------------------------")

#bazı metodlar
print(n.arange(10,45,3))#bildiğimiz range fonksiyonu gibi ama numpy dizisi şeklinde oluşturur
print(n.zeros(10)) # 10 tane 0 dan oluşan dizi oluşturur
print(n.zeros((10,10))) # 10x10 luk 0 lardan oluşan dizi oluşturur
print("-------------------------------------------------------------")
print(n.ones((10,10))) # bu da aynı zeros gibi 1 lerden oluşan dizi oluşturur
print("-------------------------------------------------------------")

print(n.linspace(0,50,32,True)) # fonksiyon da başlangıç,bitiş ve adet sayısı bilgileriyle o aralıkta adet sayısı kadar sayı oluşturur.
#bu sayıların arasındaki sayı neredeyse eşittir, sondaki True ise bitiş değerinin kapalı aralık olup (kapalı:True,açık:false) olmayacağını belirtir
print("-------------------------------------------------------------")

print(n.eye(10,M=7,k=2)) # diyagonal kısmı 1 lerle doldurulmuş geri kalanı 0 olan bir dizi oluşturur
#ilk değer dizinin kaça kaçlık olacağını belirtir(kare) eğer M değeri belirtilirse dizinin eni o boyutta olur
#k değeri ise 1 leri kaç satır yuarı çıkaracağını gösterir.
print("-------------------------------------------------------------")
#numpy.random 
print(n.random.randn(3,3)) #randn metodu kendisine verilen boyutta rastgele dizi oluşturur
print(n.random.randint(23,99,5)) #randint ise başlangıç,bitiş değerleri arasında verilen sayı kadar rastgele sayıdan oluşan diz oluşturur




