import math
import time

def quadrature_successive(x, n):
     if n < 0:
          return quadrature_successive(1/x, -n)
     elif n == 0:
          return 1
     elif n == 1:
          return x
     elif n % 2 == 0:
          return quadrature_successive(x*x, math.ceil(n/2))
     elif n % 2 == 1:
          return x * quadrature_successive(x*x, math.ceil((n-1)/2))

def exponential(x, n):
     result = 1
     for _ in range(n):
          result = result * x
     return result
     
if __name__ == '__main__':

     x, n = 10000, 100000

     start = time.time()
     r1 = quadrature_successive(x, n)
     stop = time.time()

     print("Quadrature Successive (s): ", stop-start)

     start = time.time()
     result = 1
     for i in range(n):
          result = result * x
     stop = time.time()

     print("Moltiplicazioni Successive (s): ",stop-start)

