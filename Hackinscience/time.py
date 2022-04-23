from time import time
from math import sqrt
start_time=time()
for i in range(100000000,1000090000):
    teorem=False
    for j in range(2,int(sqrt(i))+1,1):
        if i % j==0:
            teorem=True
    if teorem==False:
        print(i,"%.5f" % (time() - start_time))
        break