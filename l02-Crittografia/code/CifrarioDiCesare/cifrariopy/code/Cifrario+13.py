from utils import from_char_to_value, from_value_to_char, create_otp_key

def cifrario_di_cesare(msg):
    msg = msg.upper()
    output = ""
    for l in msg:
        if not(l in [' ', '.', ',', '!', '?']):
            v = (from_char_to_value(l) + 13) % 26
            l = from_value_to_char(v)
        output += l
    return output

print(cifrario_di_cesare('Silvia, rimembri ancora?'))
print(cifrario_di_cesare('URYYB URYYB'))
