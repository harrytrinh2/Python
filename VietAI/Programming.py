#Bibonacci
def fibR(n):
    if n == 1 or n == 2:
        return 1
    return fibR(n - 1) + fibR(n - 2)
n=21
for i in range(1,n,1):
    print(fibR(i))

#Find the occurrence of number in array
import numpy as np
I=np.array([[3,4,5,99],[99,12,10,5],[5,1,14,33]])
print((I==5).sum())
print((I==99).sum())

#square root without using function
def double_square_root(num):
    x1 = (num * 1.0) / 2
    x2= (x1 + (num / x1)) / 2
    while(abs(x1 - x2) >= 0.0000001) :
        x1 = x2
        x2 = (x1 + (num / x1)) / 2
    return x2
print(double_square_root(6))

#Check doi xung
num = '19++91'
val = len(num)
if num == str(num)[::-1]:
    print('day la day doi xung')
else:
    print('day KO la day doi xung')

#Rand() Create random function
import time
def tt(num):
    sec = time.time()
    sec=sec % 3600
    if (num >= sec):
        print("%ld\n", sec)
    sec = sec % num
    return sec
for i in range(1,9,1):
    print(tt(i))