import random as rnd
import string
import math
import time

def otp_simple_enc(msg, key):
     result = ''
     msg=msg.upper()
     for i in range(len(msg)):
          if key[i] == '0':
               value = ( from_char_to_value(msg[i]) - 1 ) % 26
               lettera = from_value_to_char(value)
               result += lettera
          elif key[i] == '1':
               value = (from_char_to_value(msg[i]) + 1) % 26
               lettera = from_value_to_char(value)
               result += lettera
     return result

def otp_simple_dec(msg, key):
     result = ''
     
     msg=msg.upper()
     for i in range(len(msg)):
          if key[i] == '0':
               value = (from_char_to_value(msg[i]) + 1) % 26
               lettera = from_value_to_char(value)
               result += lettera
          elif key[i] == '1':
               value = (from_char_to_value(msg[i]) - 1) % 26
               lettera = from_value_to_char(value)
               result += lettera
     return result

def from_value_to_char(n):
     alphabet = list(string.ascii_uppercase)
     return alphabet[n]


def from_char_to_value(c):
     alphabet = list(string.ascii_uppercase)
     return alphabet.index(c)

def otp2_enc(msg, key):
     result = ''
     msg=msg.upper()
     for i in range(len(msg)):
          c = from_char_to_value(msg[i])
          k = from_char_to_value(key[i])
          result += from_value_to_char((c+k)%26)
     return result

def otp2_dec(msg, key):
     result = ''
     msg=msg.upper()
     for i in range(len(msg)):
          c = from_char_to_value(msg[i])
          k = from_char_to_value(key[i])
          result += from_value_to_char((c-k)%26)
     return result


def otp(msg, key):
     result = ''
     msg=msg.upper()
     for i in range(len(msg)):
          result += chr(ord(msg[i]) ^ ord(key[i]))
     return result


def create_key(length, seed=0):
     key = ''
     rnd.seed(seed)
     for i in range(length):
          key += rnd.choice(list(string.ascii_uppercase))
     return key

def create_binary_key(length, seed=0):
     key = ''
     rnd.seed(seed)
     for i in range(length):
          key += str(rnd.randint(0,1))
     return key

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
     for i in range(n):
          result = result * x
     return result

start = time.time()
print(quadrature_successive(30000, 75000))
stop = time.time()

print(stop-start)

start = time.time()
print(quadrature_successive(30000, 75000))
stop = time.time()

print(stop-start)

print(create_key(10))

alphabet = list(string.ascii_uppercase)
print(len(alphabet))

key = create_key(100)


cifrato = otp2_enc('ciao',key)

print(cifrato)
print(otp2_dec(cifrato,key))

