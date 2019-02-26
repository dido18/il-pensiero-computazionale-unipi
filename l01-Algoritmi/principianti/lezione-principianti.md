<!-- $size: 16:9 -->

Dall'Algoritmo al Codice
===


<center>
	<img src=./img/copertina.jpg width="500">
</center>

##### [Il Pensiero Computazionale](http://ilpensierocomputazionale.di.unipi.it/)
###### Percorso Formativo per i Docenti della Scuola Secondaria di II Grado
#### Lezione 1 - Parte 2
<sub><sup>[Stefano Forti](http://pages.di.unipi.it/forti) and  [Davide Neri](http://pages.di.unipi.it/neri/)</sup></sub>

---
# Sommario
Risoveremo insieme i seguenti problemi in Python:
  1. Problema dalle Olimpiadi della Matematica
  2. Quick sort
  3. Merge sort

---
# Un problema dalle Olimpiadi della Matematica (2015)

<center>
	<img src=./img/graffette.png width="1024">
</center>

### Lavoro di Squadra!
###### Provate a risolvere il problema :smile:

---
# Suggerimento

Federica può applicare al mucchio di graffette ciascuna di queste due funzioni ripetutamente:

$$f(n) = n - 3\ \ if\ n\geqslant 3$$
$$g(n) = n/2\ \ if\ n=2k$$

Federica vince se rimangono $0$ graffette. Ciò è possibile se e solo se, alla penultima mossa, ci sono $3$ graffette sul tavolo.

<center>
	<img src=./img/clips.jpg width="300">
</center>

---
# Soluzione

I numeri buoni sono dunque tutti quelli nell'intervallo $[3, 2015]$ che portano a $3$ graffette residue con una certa sequenza di applicazioni di $f$ e $g$.

Le possiamo generare (e contare!) semplicemente col seguente codice Python.

```python
soluzione = [0] * 2015 # crea una lista con 2015 zeri
soluzione[3] = 1

for i in range(3, 2015):
   if (soluzione[i] == 1):
      solUno = i * 2 # un numero a cui applicare g
      solDue = i + 3 # un numero a cui applicare f
   
      if (solUno < 2015):
         soluzione[solUno] = 1
      if (solDue < 2015):
         soluzione[solDue] = 1

print(sum(soluzione))
```
---
# Come si risolve (b)?

```python
soluzione = [0] * 2015
soluzione[1] = 1

for i in range(1, 2015):
   if (soluzione[i] == 1):
      solUno = i * 2 # un numero a cui applicare g
      solDue = i + 3 # un numero a cui applicare f
      if (solUno < 2015):
         soluzione[solUno] = 1
      if (solDue < 2015):
         soluzione[solDue] = 1

print(sum(soluzione))
```

---
# Una soluzione per il caso generale?

Scriviamo una **funzione** Python per risolvere il caso generale, specificando il totale delle graffette ```numGraffette``` e le graffette che da lasciare per vincere ```numVittoria```.

```python
def trovaVittorie(numGraffette, numVittoria):                
   soluzione = [0] * numGraffette
   soluzione[numVittoria] = 1

   for i in range(1, numGraffette):
      if (soluzione[i] == 1):
         solUno = i * 2 # un numero a cui applicare g
         solDue = i + 3 # un numero a cui applicare f
         if (solUno < 2015):
            soluzione[solUno] = 1
         if (solDue < 2015):
            soluzione[solDue] = 1
            
   return sum(soluzione)

print(trovaVittorie(2015, 3)) # soluzione di (a)
print(trovaVittorie(2015, 1)) # soluzione di (b)
```

---

# Il Problema dell'Ordinamento

Ordinare significa riposizionare $n$ elementi di una certa collezione secondo un dato ordine.


Vedremo e confronteremo due algoritmi di ordinamento:

- *Insertion Sort* (o ordinamento per inserimento) con complessità quadratica $O(n^2)$
- *Quick Sort* (o ordinamento veloce) con complessità linearitmica $O(n \lg n)$

<center>
	<img src=./img/bigoh.bmp width="400">
</center>

---
# Insertion Sort (Idea)

:bulb: *E' l'algoritmo con cui si riordina una mano di carte.*

<center>
	<img src=./img/cards.bmp width="300">
</center>

Consta di tre passi:
1. Rimuovi un elemento dalla collezione.
2. Confrontalo coi successivi finché non trovi il suo posto nell'attuale configurazione.
3. Ripeti finchè non sono finiti gli elementi.

---
# Insertion Sort (Complessità)

Se la collezione è già ordinata (caso ottimo) si impiega un tempo propozionale al numero di elementi, cioè $O(n)$.

Se, invece, la sequenza è ordinata al contrario (caso pessimo) si impiega un tempo proporzionale al quadrato degli elementi da ordinare, cioè $O(n^2)$. 

Infatti, al caso pessimo, si deve confrontare l'$i$-esimo elemento con gli $i-1$ successivi. Ovvero:

$$\sum^n_{i=1} (n-i)= \sum^{n-1}_{j=1} j = \frac{n (n-1)}{2} = O(n^2)$$


---
# Insertion Sort (Demo)

<center>
<iframe width="750" height="550" src=./img/"https://www.youtube.com/embed/ROalU379l3U" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>

###### [Insert-sort with Romanian folk dance](https://www.youtube.com/embed/ROalU379l3U)


---
# Insertion Sort (Pseudo-codice)

<center>
	<img src=./img/insertionsort.png width="1024">
</center>

:books: Provate voi a eseguire il codice sulla lista ```[54,26,93,17,77,31,44,55,20]``` e implementate la funzione Python ```insertionSort(A)```.

---
# Insertion Sort (Codice)

```python
def insertionSort(A):
   for j in range(1,len(A)):

     key = A[j]
     i = j - 1

     while i >= 0 and A[i] > key: # rispetto allo pseudocodice gli indici partono da 0
         A[i+1]=A[i]
         i = i - 1

     A[i+1] = key
```

###### Esempio:
```python
unaLista = [54,26,93,17,77,31,44,55,20]
insertionSort(unaLista)
print(unaLista)
```

---
# Prendere il tempo!

:hourglass: In Python possiamo cronometrare la durata di esecuzione di un programma. Basta importare la libreria ```time``` e usare la funzione ```time.time()``` come nell'esempio qui sotto:

```python
import random as rnd
import time

unaLista = []

# generiamo una lista di 10000 interi a caso 
for i in range(10000):
   unaLista.append(rnd.randint(1,100000))
    
start = time.time() # segna il tempo di inizio nella variabile start
insertionSort(unaLista)
stop = time.time() # segna il tempo di fine nella variabile start
print('Insertion sort per', stop-start, "secondi.")
```

---
# Quick Sort (Idea)

Quick Sort è tra gli algoritmi più usati per l'ordinamento. 

Utilizza un approccio *divide et impera*. 

:bulb: *L'algoritmo divide la collezione in due parti, poi le ordina indipendentemente.*

L'idea di base segue due passi:

1. Sceglie un elemento $p$ (*pivot*) nella collezione e la divide in due sotto-collezioni, una con gli elementi $e \leqslant p$, l'altra con gli elementi $e \gt p$. Complessità: $O(n)$.

<center>
	<img src=./img/qsortidea.png width="750">
</center>

2. Ripete (1) sulle due metà.

---
# Quick Sort (Complessità)

Se ogni volta scegliamo $p$ tale che la collezione si divide in $9/10$ e $1/10$, un caso abbastanza sbilanciato, e ogni volta la partizione delle sotto-collezioni ci costa $O(n)$, la complessità è:

$$O(n)\cdot \log_{10}n + O(n)\cdot \log_{10/9}n \simeq O(n\lg n)$$

<center>
	<img src=./img/qsortcomplexity.png width="600">
</center>

---
# Quick Sort (Demo)

<center>
<iframe width="750" height="550" src=./img/"https://www.youtube.com/embed/ywWBy6J5gz8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>

###### [Quick-sort with Hungarian folk dance](https://www.youtube.com/watch?v=ywWBy6J5gz8)

---
# Quick Sort (Pseudo-codice)

###### Quick Sort
<center>
	<img src=./img/qsortpc.png width="350">
</center>


###### Partizionamento lineare
<center>
	<img src=./img/partitionpc.png width="400">
</center>

--- 
# Quick Sort (Codice)

```python
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:
       splitpoint = partition(alist,first,last)
       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)
```
---

```python
def partition(alist,first,last):
   pivotvalue = alist[first]
   leftmark = first+1
   rightmark = last
   done = False
   
   while not done:
       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1
       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1
       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp
           
   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp

   return rightmark
```

---
# Quick Sort (Esempio)

```python
alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)
```

---
# Prendiamo i tempi!

```python
import random as rnd
import time

unaLista = []
for i in range(10000):
   unaLista.append(rnd.randint(1,100000))
    
start = time.time() # segna il tempo di inizio nella variabile start
insertionSort(unaLista)
stop = time.time() # segna il tempo di fine nella variabile start
print('Insertion Sort per', stop-start, "secondi.")

unaLista = []
for i in range(10000):
   unaLista.append(rnd.randint(1,100000))
   
start = time.time() # segna il tempo di inizio nella variabile start
quickSort(unaLista)
stop = time.time() # segna il tempo di fine nella variabile start
print('Quick Sort per', stop-start, "secondi.")
```

---
# Merge Sort

La funzione di libreria ```sorted()``` di Python implementa una variante del Merge Sort visto in classe.

Provate a prendere i tempi di questa variante del Merge Sort! 

```python
unaLista = []
for i in range(10000):
   unaLista.append(rnd.randint(1,100000))
   
start = time.time() # segna il tempo di inizio nella variabile start
sorted(unaLista)
stop = time.time() # segna il tempo di fine nella variabile start
print('Merge Sort per', stop-start, "secondi.")
```

---
# Esercizio

Si può ordinare in tempo lineare $O(n)$ conoscendo l'intervallo $[0, M]$ in cui si trovano i numeri da ordinare?


---
# La morale è ancora quella...

> **Algoritmi efficienti** sono da considerarsi migliori di **computer potenti**.
> O, ancora, l'accoppiata vincente è **algoritmi efficienti** su **computer potenti**.
> 

<br>
</br>


<center>
	<img src=./img/comparison.png width="1024">
</center>

---
# Esercizi

1. Data una stringa ```S```, come si può stabilire se è palindroma? Scrivere lo pseudocodice e il codice della funzione ```def palindromo(s):``` che restituisce ```True``` se la parola è palindroma e ```False``` altrimenti.

2. Date due stringhe ```A``` e ```B```, come si può stabilire se una è l'anagramma dell'altra? Esistono almeno quattro soluzioni rispettivamente di complessità esponenziale $O(2^n)$, quadratica $O(n^2)$, linearitmica $O(n\lg n)$ e lineare $O(n)$. Scrivere lo pseudocodice di almeno due soluzioni e implementare la più efficiente.

3. Data una lista $D$ di $n$ interi (positivi e negativi), come si può stabilire la sottolista di somma massima, i.e. come possiamo decidere $a$ e $b$ tali da ottenere il massimo $\max \limits_{a,b \in \mathbb{N}_{n}}\{\sum_{i=a}^b D[i]\}$. Esistono almeno tre soluzioni rispettivamente di complessità cubica $O(n^3)$, quadratica $O(n^2)$ e lineare $O(n)$. Scrivere lo pseudocodice di almeno due soluzioni e implementare la più efficiente.
