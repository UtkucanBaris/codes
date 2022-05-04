"""1.TC kimlik no 11 haneden oluşur
   2.İlk rakam sıfır olamaz
   3.İlk 10 rakamın birler basamağı 11. rakamı vermektedir.
   4. 1,3,5,7 ve 9.cu hanelerin toplamının 7 ile çarpımından 2,4,6
   ve 8. haneler çıkartıldığında geriye kalan sayının birler
   basamağı 10. haneyi verir
   Tc kimlik numarasının doğru olup olmadığını söyleyen program yaz"""
import timeit
def Tckontrol():print("Tc kimlik numarasında harf olamaz");exit()
while True:
    print("Çıkmak için herhangi bir harf yazın",end="\n\n")
    Tc=[i if i.isdecimal()==True and i !="" else Tckontrol() for i in input("Tc kimlik numarası giriniz: ")]
    start=timeit.default_timer()
    if Tc != "" and len(Tc)==11 and Tc[0] != 0: # 1 ve 2.ci koşul burada
        kont3=(sum(list(map(int,Tc[0:10]))))%10#ilk 10 rakamı topluyorum toplamlarının birler basamağını alıyorum
        if str(kont3) == Tc[10]: # 3. koşul burada        
            kont4 = (((sum(list(map(int,Tc[0:10:2]))))*7)-(sum(list(map(int,Tc[1:9:2])))))%10 #4.koşul
            if str(kont4) == Tc[9]: # 4.koşulun 10.hanesini kontrol
                print("Bu Tc kimlik numarası {tc} geçerlidir" .format (tc="".join(Tc)));print()
            else:print("Hata girdiğiniz Tc kimlik numarası {tc} geçersizdir" .format (tc="".join(Tc)));print()
        else:print("Hata girdiğiniz Tc kimlik numarası {tc} geçersizdir" .format (tc="".join(Tc)));print()
    else:print("Hata, girdiğiniz numara {tc} sıfır ile başlayamaz ve 11 karakterli olmalıdır" .format (tc="".join(Tc)));print()
    print("Time :",timeit.default_timer()-start)
