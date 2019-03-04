from utils import from_char_to_value, from_value_to_char
import random as rnd

def otp_simple_encrypt(msg, key):
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

def otp_simple_decrypt(msg, key):
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

def create_binary_key(length, seed=0):
    """Generate a key of zero and ones of length.
    """
    key = ""
    rnd.seed(seed)
    for _ in range(length):
        key += str(rnd.randint(0,1))
    return key

if __name__ == '__main__':
    msg = "ciao" #input("Message: ")
    #key = "0101" # input("Key: ")
    key = create_binary_key(len(msg))

    cifrato = otp_simple_encrypt(msg, key)
    print("Messaggio cifrato: ", cifrato)
    print("Messaggio decifrato: ", otp_simple_decrypt(cifrato,key))