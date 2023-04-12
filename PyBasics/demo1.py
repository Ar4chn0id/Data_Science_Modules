import random as r


newlist = list(range(0,10))
print(newlist)

print(newlist[r.randint(0,10)])
    
r.shuffle(newlist)

print(newlist)

print("----------------------------------------------------")
#zip fonksiyonu

liste1 =["merhaba","dünya","nasılsın"]
liste2 =[1,2,3]
liste3 =["a","b","c"]

#zip fonksiyonu listeleri indexine göre eşleştirir ve tuple içeren liste(type:zip) şeklinde döndürür
liste4=zip(liste1,liste2,liste3)

print("içerdeki elemanın türü: ",type(list(liste4)[1]))

for (index,eleman) in enumerate(liste4):
    print(f"index: {index}, eleman: {eleman}")


liste_ornegi = [member * 3 for member in range(5,10)]
print(liste_ornegi)


print("----------------------------------------------------")

# args & kwargs
def func1(*args):
    return sum(args)
print(func1(1,2,3,4,5,6,78,90,52345,4,435423))

def func2(*args):
    return args
print(type(func2(1,2,4,2)))

def func3(**kwargs):
    return kwargs
print(type(func3(a=1,b=2,c=3)))
print(func3(a=1,b=2,c=3))

print("----------------------------------------------------")
# map fonksiyonu

listem = [i for i in range(10)]

def fonksiyon(arg):
    return arg+10
    
yeni_listem=list(map(fonksiyon,listem)) #map kendisine verilen fonksiyona kendisine verilen listedeki bütün elemanları vererek çalıştırır ve sonuçları bir map objesi şeklinde döndürür(map objesi listeye çevrilebilir)

#burda bilemdiğim bazı temel özellikleri not aldım
print(listem)
print(yeni_listem)

#filter fonksiyonu da argümanları map gibi alır(bi fonksiyon bi liste) ancak listedeki elemanlardan hangileri fonksiyondan true değerini döndürürse onları fiter olarak döndürür(list e çevrilebiliyor bu da)

def ciftmi(sayi):
    return sayi %2 ==0

x=filter(ciftmi,listem)
print(list(x))

print("----------------------------------------------------")
#lambda gösterimi
#tek satırda fonksiyon tanımlamana olanak sağlar

fonksiyon2 = lambda arguman : arguman*2 # ilki fonksiyona verilecek parametreyi ikincisi yani iki nokta dan sonrası döndürülecek işlemi temsil eder

# ornek kullanım
orneklerlistesi= [1,2,3,4,5]

x=list(map(lambda i : i**2,orneklerlistesi))

print(x)