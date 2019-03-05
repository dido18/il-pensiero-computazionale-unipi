import string
import random 

def from_value_to_char(n):
     alphabet = list(string.ascii_uppercase)
     return alphabet[n]

def from_char_to_value(c):
     alphabet = list(string.ascii_uppercase)
     return alphabet.index(c) 


def create_otp_key(length, seed=0):
     key = ''
     random.seed(seed)
     for _ in range(length):
          key += random.choice(list(string.ascii_uppercase))
     return key