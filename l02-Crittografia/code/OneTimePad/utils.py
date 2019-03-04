import string

def from_value_to_char(n):
     alphabet = list(string.ascii_uppercase)
     return alphabet[n]

def from_char_to_value(c):
     alphabet = list(string.ascii_uppercase)
     return alphabet.index(c) 