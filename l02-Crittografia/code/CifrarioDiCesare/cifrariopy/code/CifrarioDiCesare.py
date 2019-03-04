message = input("Inserisci il mesasggio da decodificare o codificare: ") # Get a message
message = message.upper()           # Make it all UPPERCASE :)
output = ""
encode = input("inserisci `c` per codificare e `d` per decodificare: ") # Get a message

if encode == "c":
    op = +1
else:
    op = -1

for letter in message:
    value = ord(letter) + (op*2)
    letter = chr(value)
    if not letter.isupper():
        value = value + (-1*op*26)
        letter = chr(value)
    output += letter

print("risultato: ", output)   # Output our coded/decoded message
