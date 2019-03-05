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

Un _cifrario_ è un codice segreto che trasforma un messaggio in modo da renderlo incomprensibile a chi non conosce la chiave del codice.

Giulio Cesare (100-44 a.C.) inviava messaggi facendo "scorrere" l'alfabeto come mostrato dall'anello qui sotto:

<center>
	<img src=./img/cifrario.bmp width="300">
</center>

La _chiave_ del cifrario (o _rotazione_) è rappresentata dal numero di posizioni $k$ di cui far scorrere ciascuna lettera del messaggio ($k=13$ nell'esempio).

---
# Cifrario Simmetrico

Scegliendo $k=13$ come chiave, 

Giulio Cesare (100-44 a.C.) inviava messaggi facendo "scorrere" l'alfabeto come mostrato dall'anello qui sotto:

<center>
	<img src=./img/cifrario.bmp width="300">
</center>

La _chiave_ del cifrario (o _rotazione_) è rappresentata dal numero di posizioni $k$ di cui far scorrere ciascuna lettera del messaggio ($k=13$ nell'esempio).