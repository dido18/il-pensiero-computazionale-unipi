<!-- $size: 16:9 -->
<!-- page_number: true -->

Crittografia
===
<center>
	<img src=./img/copertina.jpg width="500">
</center>

##### [Il Pensiero Computazionale](http://ilpensierocomputazionale.di.unipi.it/)
###### Percorso Formativo per i Docenti della Scuola Secondaria di II Grado
#### Lezione 3
<sub><sup>[Stefano Forti](http://pages.di.unipi.it/forti) and  [Davide Neri](http://pages.di.unipi.it/neri/)</sup></sub>

---
# Cosa faremo oggi ?
Sommario:
 - \[Intro Python\]
 - Cifrario di Cesare 
 - OneTimePad 
 - Diffie - Hellman: esponenziazione per quadrature successive

---
# Cifrario di Cesare

Un _cifrario_ Ã¨ un codice segreto che trasforma un messaggio in modo da renderlo incomprensibile a chi non conosce la chiave del codice.

Giulio Cesare (100-44 a.C.) inviava messaggi facendo "scorrere" l'alfabeto come mostrato dall'anello qui sotto:

<center>
	<img src=./img/cifrario.bmp width="300">
</center>

La _chiave_ del cifrario (o _rotazione_) Ã¨ rappresentata dal numero di posizioni $k$ di cui far scorrere ciascuna lettera del messaggio ($k=13$ nell'esempio).

---
# Cifrario Simmetrico

Scegliendo $k=13$ come chiave, 



---
# One Time Pad (OTP)- il "cifrario perfetto"
Utilizzato per le comunicazioni tra le spie durante la guerra.
Venivano equipaggiati di taccuini ("pad" in inglese) contenenti una lunga chiave per ogni pagina, da poter strappare una volta utilizzata ("one time", ovvero "un solo uso").
<center>
	<img src=./img/otp.png width="500">
</center>

---
# One Time Pad (OTP) - il "cifrario perfetto"
Tecnica di crittografia inattaccabile (comprovata da una dimostrazione matematica).
 
La chiave deve essere:
 - **random**
 - lunga **almeno quanto** il messaggio
 - **non riutilizzabile**.
 - **segreta e condivisa** trale parti.



---
# One Time Pad (OTP) - forma classica

Ad ogni lettera viene associato un numero. 

| A | B | C | D | E | F | G | H | I | J | K  | L  | M  | N |
|:-:|---|---|---|---|---|---|---|---|---|----|----|----|---|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13

| O |  P| Q | R | S | T | U | V | W | X  | Y  | Z  | 
|:-:|---|---|---|---|---|---|---|---|----|----|----|
| 14 | 15 | 16 | 17 | 18 | 19 | 20 |21 |22 | 23 | 24 | 25 |

*Encryption*:  Ogni lettera del testo in chiaro, viene trasformato nel valore numero `m`. Ogni lettera della chiave viene trasnfomrato nel valore numero `k`. Poi per ogni carattere si effettua la seguente operazione:
```c + k mod 26```
*Decryption*: `c - k mod 26`




---
# One Time Pad (OTP) - Esempio

| A | B | C | D | E | F | G | H | I | J | K  | L  | M  | N |
|:-:|---|---|---|---|---|---|---|---|---|----|----|----|---|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13

| O |  P| Q | R | S | T | U | V | W | X  | Y  | Z  | 
|:-:|---|---|---|---|---|---|---|---|----|----|----|
| 14 | 15 | 16 | 17 | 18 | 19 | 20 |21 |22 | 23 | 24 | 25 |

```sh
# encryption
Testo in chiaro: C I A O  | 2 8 0 14
Chiave:          A J R F  | 0 9 17 5
------------------------------------
Testo cifrato:   C R R T  | 2 17 17 19

# decryption
Testo cifrato:   C R R T  | 2 17 17 19
Chiave:          A J R F  | 0 9  17 5
-----------------------------------
Testo in chiaro: C I A O  | 2 8  0 4
```

---
# One Time Pad (OTP) - Esercizio

prova a decifrare il messaggio, di cosa si stratta ?
```sh
cifrato: CSRMZQBACNAWSMEHRGMPHBPVRNEKNDJGUJDXLZEXHNXRSIUKBSVNGKAJHINEKGYAQOZKSGUAH

key:   MYNBIQPMZJPLSGQEJEYDTZIRWZTEJDXCVKPRDLNKTUGRPOQIBZRACXMWZVUATPKHXKWCGSHHZ

text: ???
```
---
# One Time Pad (OTP) - Con carta igienica :)
Come fare:
- comprare due rotoli di carta igienica e due pennarelli.
- incontrarsi in un luogo segreto e scrivere una chiave **segreta** su ciascuno dei due rotoli (una lettera per ogni strappo)

### GIOCO A SQUADRE !!!
<center>
	<img src=./img/carta.jpg width="300">
</center>


---
# One Time Pad (OTP) - In Python

```python
import string

# converte il carattere c nel valore numerico
def from_char_to_value(c):
     alphabet = list(string.ascii_uppercase)
     return alphabet.index(c)
     
# converte il valore numerico n nel carattere 
def from_value_to_char(n):
     alphabet = list(string.ascii_uppercase)
     return alphabet[n]

```

---
# One Time Pad (OTP) - In Python

```python
def otp_encrypt(msg, key):
     result = ''
     msg=msg.upper()
     for i in range(len(msg)):
          c = from_char_to_value(msg[i])
          k = from_char_to_value(key[i])
          result += from_value_to_char((c + k) % 26)
     return result

def otp_decrypt(msg, key):
     result = ''
     msg=msg.upper()
     for i in range(len(msg)):
          c = from_char_to_value(msg[i])
          k = from_char_to_value(key[i])
          result += from_value_to_char((c - k) % 26)
     return result
```
---
# One Time Pad (OTP) - In Python
```
msg = "CIAO" 
key = "AJRF" 

cifrato = otp_encrypt(msg, key)
print("Messaggio cifrato: ", cifrato)
inchiaro =  otp_decrypt(cifrato, key)
print("Messaggio decifrato: ", inchiaro)
```
