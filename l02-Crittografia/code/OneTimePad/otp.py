from utils import from_char_to_value, from_value_to_char

def otp_encrypt(msg, key):
     result = ''
     msg=msg.upper()
     for i in range(len(msg)):
          c = from_char_to_value(msg[i])
          k = from_char_to_value(key[i])
          result += from_value_to_char((c+k)%26)
     return result

def otp_decrypt(msg, key):
     result = ''
     msg=msg.upper()
     for i in range(len(msg)):
          c = from_char_to_value(msg[i])
          k = from_char_to_value(key[i])
          result += from_value_to_char((c-k)%26)
     return result
    

if __name__ == '__main__':
    
    msg = "ciao" #input("Message: ")
    key = "ZUBQ" # input("Key: ")

    cifrato = otp_encrypt(msg, key)
    print("Messaggio cifrato: ", cifrato)
    print("Messaggio decifrato: ", otp_decrypt(cifrato,key))