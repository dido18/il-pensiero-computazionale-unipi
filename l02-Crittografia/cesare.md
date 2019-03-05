<!-- $size: 16:9 -->
<!-- page_number: true -->

Crittografia
===
<center>
	<img src=./img/copertina.jpg width="500">
</center>

##### [Il Pensiero Computazionale](http://ilpensierocomputazionale.di.unipi.it/)
###### Percorso Formativo per i Docenti della Scuola Secondaria di II Grado
#### Lezione 3 (per tutti)
<sub><sup>[Stefano Forti](http://pages.di.unipi.it/forti) and  [Davide Neri](http://pages.di.unipi.it/neri/)</sup></sub>

---
# Cosa faremo oggi ?
Sommario:
 - \[Intro Python\]
 - Cifrario di Cesare 
 - OneTimePad 
 - Diffie - Hellman: esponenziazione per quadrature successive

---
# Cifrario di Cesare (Idea)

Un _cifrario_ è un codice segreto che trasforma un messaggio in modo da renderlo incomprensibile a chi non conosce la chiave del codice.

Giulio Cesare (100-44 a.C.) inviava messaggi facendo "scorrere" l'alfabeto come mostrato dall'anello qui sotto:

<center>
	<img src=./img/cifrario.bmp width="300">
</center>

La _chiave_ del cifrario (o _rotazione_) è rappresentata dal numero di posizioni $k$ di cui far scorrere ciascuna lettera del messaggio ($k=13$ nell'esempio).

---
# Cifrario Simmetrico

Scegliendo $k=13$ come chiave, otteniamo che $l \rightarrow l'$ e che $l' \rightarrow l$ dove $l, l'$ rappresentano lettere dell'alfabeto.

<center>
	<img src=./img/cifrario.bmp width="300">
</center>

Un cifrario di questo tipo si dice _simmetrico_ in quanto permette di **crittare** e **decrittare** un messaggio eseguendo la stessa operazione.

Per esempio: ```HELLO``` $\rightarrow$ ```URYYB```$\rightarrow$ ```HELLO```.

---
# Due Utili Funzioni

Per il laboratorio di oggi, iniziamo col definire due funzioni molto utili hanno bisogno di

```python
import string
```

La prima funzione, dato un numero ```n``` tra ```0``` e ```25```, ci restituisce il carattere dell'alfabeto inglese in quella posizione:

```python
def from_value_to_char(n):
     alphabet = list(string.ascii_uppercase)
     return alphabet[n]
```

La seconda, dato un carattere ```c```, ci restituisce la sua posizione nell'alfabeto inglese:

```python
#TODO: provate a scriverla voi...
def from_char_to_value(c):

```

---
# Due Utili Funzioni

Per il laboratorio di oggi, iniziamo col definire due funzioni molto utili hanno bisogno di

```python
import string
```

La prima funzione, dato un numero ```n``` tra ```0``` e ```25```, ci restituisce il carattere dell'alfabeto inglese in quella posizione:

```python
def from_value_to_char(n):
     alphabet = list(string.ascii_uppercase)
     return alphabet[n]
```

La seconda, dato un carattere ```c```, ci restituisce invece la sua posizione nell'alfabeto inglese:

```python
def from_char_to_value(c):
     alphabet = list(string.ascii_uppercase)
     return alphabet.index(c) 
```

---
# Cifrario di Cesare (Codice)

```python
def cifrario_di_cesare(msg):
    msg = msg.upper()
    output = ""
    for l in msg:
    
        #TODO: completare il codice in modo da gestire anche [' ', '.', ',', '!', '?']
        
        output += l
    return output
```

---
# Cifrario di Cesare (Codice)

```python
def cifrario_di_cesare(msg):
    msg = msg.upper()
    output = ""
    for l in msg:
        if not(l in [' ', '.', ',', '!', '?']):
            v = (from_char_to_value(l) + 13) % 26
            l = from_value_to_char(v)
        output += l
    return output
    
print(cifrario_di_cesare('URYYB, URYYB!'))
```



---
# Prova Tu!

A chi è destinato il messaggio che Eva ed Eustachio hanno rubato a una famosa spia internazionale?
<center>
<h2> FVYIVN, EVZRZOEV NAPBEN? </h2>
<center>
<center>
  <img src=./img/agents.png width="300"> 
</center>




