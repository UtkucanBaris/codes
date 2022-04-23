# Check if the number is prime or not
# //-------------------------------\\
# def is_prime(n):
#     return n > 1 and all(n%i!=0 for i in range(2, int(n**0.5)+1))
# //---------------------------------------\\

# Check if the number is prime or not
# //---------------------------------------\\
# from math import sqrt
# def is_prime(n):
#     a = True
#     if n == 1:
#         return False
#     for i in range(2,int(sqrt(n))+1):
#         if n % i == 0 or n == 2 and n != 1:
#             a = False
#     return a
# if is_prime(int(input("Sayı Giriniz : "))) == True:
#     print("Asal Sayıdır")
# else:
#     print("Asal Sayı Değildir")
# //---------------------------------------\\

# //---------------------------------------\\
# def is_prime(num):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 return False
#         return True
#     else:
#         return False

# numbers = []
# for i in range(10000, 10050):
#     if is_prime(i):
#         numbers.append(i)
#     else:
#         pass
# print(*numbers, sep=', ')

# //---------------------------------------\\

# from math import sqrt
# a=[]
# for i in range(10000,10050):
#     teorem=False
#     for j in range(2,int(sqrt(i))+1,1):
#         if i % j==0:
#             teorem=True
#     if teorem==False:
#         a.append(i)
# print(*a,sep=", ")
# //---------------------------------------\\