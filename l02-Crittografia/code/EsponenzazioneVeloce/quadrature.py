import math
import time

def quadrature_successive(x, n):
     if n < 0:
          return quadrature_successive(math.ceil(1/x), -n)
     elif n == 0:
          return 1
     elif n == 1:
          return x
     elif n % 2 == 0:
          return quadrature_successive(x*x, math.ceil(n/2))
     elif n % 2 == 1:
          return x * quadrature_successive(x*x, math.ceil((n-1)/2))

def exponential(x, n):
     result = x
     for _ in range(n):
          result = result * x
     return result
     
if __name__ == '__main__':
     n = 10000
     x = 100000

     start = time.time()
     quadrature_successive(n, x)
     stop = time.time()

     print("Tempo quadrature successive (sec): ", stop-start)

     start = time.time()
     exponential(n, x)
     stop = time.time()

     print("Tempo esponenziale (sec): ",stop-start)
