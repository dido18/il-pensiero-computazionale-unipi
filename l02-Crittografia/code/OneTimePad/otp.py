from utils import from_char_to_value, from_value_to_char, create_otp_key

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
    
    msg = "CIAO" 
    key = "AJRF" 

#     cifrato = otp_encrypt(msg, key)
#     print("Messaggio cifrato: ", cifrato)
#     inchiaro =  otp_decrypt(cifrato,key)
#     print("Messaggio decifrato: ", inchiaro )

    promessi = "Quel ramo del lago di Como, che volge a mezzogiorno, tra due catene non interrotte di monti"
    promessi = promessi.replace(" ", "")
    promessi = promessi.replace(",", "")

    key = create_otp_key(len(promessi))
    print("Key: ", key)
    cifrato = otp_encrypt(promessi, key)
    print("Messaggio cifrato: ", cifrato)
    inchiaro =  otp_decrypt(cifrato, key)
    print("Messaggio decifrato: ", inchiaro)