# ilk_sayı = 5
# ikinci_sayı = a
# try:
#     sayı1 = int(ilk_sayı)
#     sayı2 = int(ikinci_sayı)
#     print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
# except ValueError:
#     print("Lütfen sadece sayı girin!")
# ------------------------
# ilk_sayı = 2
# ikinci_sayı = 0
# try:
#     sayı1 = int(ilk_sayı)
#     sayı2 = int(ikinci_sayı)
#     print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
# except ZeroDivisionError:
#     print("Bir Sayı 0'A Bölünemez")
# ------------------------

# ilk_sayı = input("ilk sayı: ")
# ikinci_sayı = input("ikinci sayı: ")
# try:
# sayı1 = int(ilk_sayı)
# sayı2 = int(ikinci_sayı)
# print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
# except (ValueError, ZeroDivisionError):
# print("Bir hata oluştu!")
# ------------------------

# while True:
#     ilk_sayı = input("ilk sayı (Programdan çıkmak için q tuşuna basın): ")
#     if ilk_sayı == "q":
#         break
#     ikinci_sayı = input("ikinci sayı: ")
#     try:
#         sayı1 = int(ilk_sayı)
#         sayı2 = int(ikinci_sayı)
#         print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
#     except (ValueError, ZeroDivisionError):
#         print("Bir hata oluştu!")
#         print("Lütfen tekrar deneyin!")
# ------------------------

# ilk_sayı = input("ilk sayı: ")
# ikinci_sayı = input("ikinci sayı: ")
# try:
#     sayı1 = int(ilk_sayı)
#     sayı2 = int(ikinci_sayı)
#     print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
# except ValueError as hata:
#     print("Sadece sayı girin!")
#     print("orijinal hata mesajı: ", hata)

# ------------------------
# bölünen = int(input("bölünecek sayı: "))
# if bölünen == 23:
#     raise Exception("Bu programda 23 sayısını görmek istemiyorum!")
# bölen = int(input("bölen sayı: "))
# print(bölünen/bölen)

print("\a")