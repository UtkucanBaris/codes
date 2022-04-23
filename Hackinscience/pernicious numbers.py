from math import sqrt
def is_prime(n):
    a = True
    if n == 1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0 or n == 2 and n != 1:
            a = False
    return a
for i in range(100,110):
    b=0
    a = bin(i)[2:]
    for j in a:
        b += int(j)
    if is_prime(b) == True:
        print(i)
    else:
        continue