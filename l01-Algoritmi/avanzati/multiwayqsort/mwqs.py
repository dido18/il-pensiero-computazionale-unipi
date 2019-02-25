import random
import time

def multikeyQS(S,k):
    if (len(S) <= 1):
        return S
    pivot_pos = random.randint(0, len(S)-1)
    pivot_char = S[pivot_pos][k]
    S1 = []
    S2 = []
    S3 = []
    for s in S:
        if (s[k] < pivot_char): 
            S1.append(s)
        elif (s[k] == pivot_char):
                S2.append(s)
        else: 
            S3.append(s)
    L1 = multikeyQS(S1,k)
    L2 = multikeyQS(S2,k+1)
    L3 = multikeyQS(S3,k)
    return L1+L2+L3

def swap(a, i, j):
   tmp = a[i]
   a[i] = a[j]
   a[j] = tmp
   
def multikeyQS2(a, lo, hi, r):
   if hi <= lo:
      return
   lt = lo
   gt = hi
   v = a[lo][r]
   i = lo + 1

   # (tri)partizionamento sull'r-esimo carattere
   while i <= gt:
      t = a[i][r]
      if t < v:
         #swap(a, lt, i)
         tmp = a[lt]
         a[lt] = a[i]
         a[i] = tmp
         lt += 1
         i += 1        
      elif t > v:
         #swap(a, i, gt)
         tmp = a[i]
         a[i] = a[gt]
         a[gt] = tmp
         gt-=1
      else:
         i+=1

   multikeyQS2(a, lo, lt-1, r)
   if ord(v) >= 0:
      multikeyQS2(a, lt, gt, r+1)
   multikeyQS2(a, gt+1, hi, r)


A = ["pippo", "abaco", "bar", "zoo", "mamma", "abc", "abaci", "zoa"]
start = time.time()
multikeyQS2(A, 0, len(A) - 1, 0)
stop = time.time()
print(A)
print('In-place MQSort', stop-start)

A = ["pippo", "abaco", "bar", "zoo", "mamma", "abc", "abaci", "zoa"]
start = time.time()
A_sorted = multikeyQS(A,0)
stop = time.time()
print(A_sorted)
print('MQSort',stop-start)

A = ["pippo", "abaco", "bar", "zoo", "mamma", "abc", "abaci", "zoa"]
start = time.time()
A_sorted = sorted(A)
stop = time.time()
print(A_sorted)
print('Python sorted()',stop-start)

file = open("280000_parole_italiane.txt","r")
B = []
for parola in file.readlines():
    parola = parola.replace('\n', '  ')
    B.append(parola)
file.close()

start = time.time()
B_sorted = multikeyQS(B,0)
stop = time.time()
print(B_sorted[0:10])
print('MQSort',stop-start)


file = open("280000_parole_italiane.txt","r")
B = []
for parola in file.readlines():
    parola = parola.replace('\n', '  ')
    B.append(parola)
file.close()

start = time.time()
B_sorted = sorted(B)
stop = time.time()
print(B_sorted[0:10])
print('Python sorted()',stop-start)



file = open("280000_parole_italiane.txt","r")
B = []
for parola in file.readlines():
    parola = parola.replace('\n', '  ')
    B.append(parola)
file.close()

start = time.time()
multikeyQS2(B, 0, len(B) - 1, 0)
stop = time.time()
print(B_sorted[0:10])
print('In place MQSort', stop-start)
    


