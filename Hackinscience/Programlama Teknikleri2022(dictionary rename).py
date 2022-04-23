"""29.3.2022"""
# cumle=input("Cümleyi giriniz :")
# a=[]
# for i in cumle:
#     if i not in a:
#         a.append(i)
# for i in a:
#     print("Bu harften",i,"Bu kadar var",cumle.count(i))

# metin=("Merhaba Nasılsınız Bu Programlama Teknikleri dersindeki kodların tekrarıdır")
# d={}
# for i in metin:
#     if i not in d:
#         d[i]=1
#     else:d[i]+=1

# v=d[" "]
# del d[" "]
# d["bosluk"]=v

# for i in d:
#     print("Bu harften",i,"Bu kadar var",d[i])

# liste1=[10,20,30,10,40,10,50,10,70]
# a=-1
# for i in liste1:
#     if 10 in liste1[a+1:]:
#         a=liste1.index(10,a+1)
#     else:
#         break
#     print(a)

# liste2 = [10,20,30,10,50,10,70]
# for i in range(len(liste2)):
#     if 10 == liste2[i]:
#         print(i)


# liste3 = [10,20,30,10,50,10,70]
# i=-1
# while True:
#     if 10 in liste3[i+1:]:
#         i=liste3.index(10,i+1)
#     else:
#         break
#     print(i)

# liste4 = [10,20,30,10,50,10,70]
# i=-1
# while True:
#     if 10 in liste4[i+1:]:
#         i=liste4.index(10,i+1)
#     else:
#         break
#     print(i)

"""------------------------------------------------------"""
"""31.3.2022"""
# deger=[]
# a=True
# while True:
#     while a==True:
#         sayı=input("Buraya sayı giriniz (Sonraki işlem için e'ye basınız) : ")
#         if sayı=="e":
#             print("Sonraki işleme geçiş ")
#             a=False
#             break
#         deger.append(int(sayı))
#     print()
#     print("Değer :",deger,"""
#     Girilen Sayılar ile ilgili:
#     1.Tamamını Topla
#     2.Küçükten Büyüğe Sırala
#     3.Büyükten Küçüğe Sırala
#     4.En Büyük sayıyı bul
#     5.En Küçük sayıyı bul
#     6.Yeni Sayı Denemek için
#     7.Çıkmak için Basınız""")
#     print()
#     menu=input("Yapmak istediğiniz işlemi giriniz : ")
#     print()
#     if   menu=="1":print("Hepsinin Toplamı :",sum(deger));print()
#     elif menu=="2":sırala = deger[:];sırala.sort();print("Sırasız Hali :",deger);print("Küçükten Büyüğe Sıralı Hali :",sırala);print()
#     elif menu=="3":sırala = deger[:];sırala.sort(reverse=True);print("Sırasız Hali :",deger);print("Büyükten Küçüğe Sıralı Hali :",sırala);print()
#     elif menu=="4":print("En Büyük sayı :",max(deger));print()
#     elif menu=="5":print("En Küçük sayı :",min(deger));print()
#     elif menu=="6":a=True;print("Yeni Sayı");print()
#     elif menu=="7":print("Çıkılıyor");print();break
"""------------------------------------------------------"""
# liste1=[1,3,5,7,9]
# liste2=[1,2,4,5,6,8]
# liste=[]
# for i in liste1:
# 	if i not in liste2:
# 		liste.append(i)
# for y in liste2:
# 	if y not in liste1:
# 		liste.append(y)
# liste.sort()
# print(liste)
"""------------------------------------------------------"""
# liste1=[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[14,15,4]]
# toplam=[]
# enbuyukdeger=[]
# deger=0
# for i in liste1:
# 	print(i,max(i),"max-",min(i),"min-",sum(i),"sum")
# 	toplam.append(sum(i))
# 	if deger < sum(i):
# 		deger=sum(i)
# 		enbuyukdeger.clear()
# 		enbuyukdeger.append(i)
# 	elif deger == sum(i):
# 		enbuyukdeger.append(i)
# print(enbuyukdeger)
"""------------------------------------------------------"""
