import string
import random as rnd

def otp(msg, key):
     result = ''
     msg=msg.upper()
     for i in range(len(msg)):
          result += chr(ord(msg[i]) ^ ord(key[i]))
     return result

def create_key(length, seed=0):
     key = ''
     rnd.seed(seed)
     for _ in range(length):
          key += rnd.choice(list(string.ascii_uppercase))
     return key


if __name__ == '__main__':
    msg = "ciao" #input("Message: ")
    #key = "0101" # input("Key: ")
    key = create_key(len(msg))

    cifrato = otp(msg, key)
    print("Messaggio cifrato: ", cifrato)
    print("Messaggio decifrato: ", otp(cifrato,key))