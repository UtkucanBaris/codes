import os
import sys
klasoradı=os.path.dirname(sys.argv[0])
dosyaismi=klasoradı + "/Python Proje Flavors.txt"
if os.path.isfile(dosyaismi) == True:
	dosya = open(dosyaismi,"r")
	for i in dosya:
		print(i)
	dosya.close()
else:
	print(dosyaismi + " diskte yok")
