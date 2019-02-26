<!-- $size: 16:9 -->

Dall'Algoritmo al Codice
===
<center>
  <img src=./img/copertina.jpg width=400>
</center>


##### [Il Pensiero Computazionale](http://ilpensierocomputazionale.di.unipi.it/)
###### Percorso Formativo per i Docenti della Scuola Secondaria di II Grado
###### Lezione 1 - Parte 2
<sub><sup>[Stefano Forti](http://pages.di.unipi.it/forti) and  [Davide Neri](http://pages.di.unipi.it/neri/)</sup></sub>

---
# Algoritmi e Python

Risovleremo tre problemi algoritmici con Python:
1. Sotto-sequenza massima (algoritmo cubico, quadratico, lineare)
2. Multi-key Quick Sort
3. Il Problema dello Zaino

--- 
# Problema: Sotto-sequenza Massima

ouough

<center>
	<img src=./img/massima.jpg width="420">
</center>



--- 
# Sotto sequenza massima (definizione formale)

> Data una lista $D$ di $n$ interi (positivi e negativi), come si può stabilire la sottolista di somma massima, ovvero come possiamo scegliere due valori, $a$ e $b$, tali da ottenere il massimo $\max \limits_{a,b \in \mathbb{N}_{n}}\{\sum_{i=a}^b D[i]\}$? 

Esistono almeno tre soluzioni rispettivamente di complessità cubica $O(n^3)$, quadratica $O(n^2)$ e lineare $O(n)$. 

:nerd_face: Scrivere lo pseudocodice di almeno due soluzioni e implementare la più efficiente.


--- 
# Algoritmo cubico (pseudocodice)

<center>
	<img src=./img/cubico.jpg width="900">
</center>


--- 
# Algoritmo cubico (Python)

```python
def cubico(d):
    n = len(d)                       # n indica il numero di elementi di d
    max_somma = -float('inf')
    a = 1
    v = 0

    for i in range(1, n):
        for j in range(i, n):
            tmp = 0  # tmp e' un valore temporaneo
            for k in range(i, j + 1):  # sommiamo gli elementi in d[i,j]
                tmp = tmp + d[k]
            if tmp > max_somma:
                max_somma = tmp
                a = i
                v = j

    print ("Il guadagno massimo e' {}".format(max_somma))
    print ("Esso si realizza nell'intervallo di giorni [{},{}]".format(a, v))
    print ("Porzione di d avente somma massima {}".format(d[a:v+1]))
 ```

--- 
# Algoritmo quadratico (pseudocodice)

<center>
	<img src=./img/quadratico.jpg width="1000">
</center>


--- 
# Algoritmo quadratico (Python)

```python
def quadratico(d):
    n = len(d)                       # n indica il numero di elementi di d
    max_somma = -float('inf')
    a = 1
    v = 0

    for i in range(1, n):
        tmp = 0                      # tmp e' un valore temporaneo
        for j in range(i, n):
            tmp = tmp + d[j]
            if tmp > max_somma:
                max_somma = tmp
                a = i
                v = j

    print ("Il guadagno massimo e' {}".format(max_somma))
    print ("Esso si realizza nell'intervallo di giorni [{},{}]".format(a, v))
    print ("Porzione di d avente somma massima {}".format(d[a:v+1]))
 ```
 
 --- 
# Algoritmo lineare (pseudocodice)

<center>
	<img src=./img/lineare.jpg width="900">
</center>

 --- 
 
# Algoritmo lineare* (Python)

```python
def lineare(d):
    n = len(d)  # n indica il numero di elementi di d
    max_somma = -float('inf')
    a = 1
    v = 0
    atmp = a  # atmp e' un indice temporaneo
    tmp = 0  # tmp e' un valore temporaneo

    for i in range(1, n):
        tmp = tmp + d[i]
        if tmp > max_somma:
            max_somma = tmp
            a = atmp
            v = i
        if tmp < 0:
            tmp = 0
            atmp = i + 1

    print ("Il guadagno massimo e' {}".format(max_somma))
    print ("Esso si realizza nell'intervallo di giorni [{},{}]".format(a, v))
    print ("Porzione di d avente somma massima {}".format(d[a:v+1]))
```
---
# Confronto tempi (sottomissione massima)



---
# Multi-key Quick Sort (Idea e Complessità)

Come si ordina una collezione $S$ di $n$ parole di lunghezza $L$?

:bulb: _L'algoritmo è simile al Quick Sort._

L'idea di base segue due passi:
1. Sceglie una stringa $p$ (_pivot_) tra quelle da ordinare e divide la collezione $S$ in tre sotto-collezioni, una $S_{\lt}$ con le stringhe $e[r] \lt p[r]$, una $S_{=}$ con le strighe $e[r] = p[r]$ la terza $S_{\gt}$ con le stringhe $e[r] \gt p[r]$.
2. Ripete (1) su $\langle S_{\lt}, r\rangle$, $\langle S_{=}, r+1\rangle$ e $\langle S_{\gt}, r\rangle$.

La complessità è di $O(D+n\lg n)$ dove $D$ è la lunghezza del prefisso distintivo di $S$ (ovvero, quello che distingue una stringa da tutte le altre).


---
# Multi-key Quick Sort (Demo)

<center>
	<img src=./img/3wayqs.PNG width="1024">
</center>

---
# Multi-key Quick Sort (Demo)

<center>
	<img src=./img/3wayqs2.PNG width="1024">
</center>

---
# Multi-key Quick Sort (Codice)

```python
def multikeyQS(S,k):
    if (len(S) <= 1):
        return S
    pivot_pos = random.randint(0, len(S)-1)
    pivot_char = S[pivot_pos][k]
    S1 = []
    S2 = []
    S3 = []
    for s in S:
        if (s[k] < pivot_char): 
            S1.append(s)
        elif (s[k] == pivot_char):
                S2.append(s)
        else: 
            S3.append(s)
    L1 = multikeyQS(S1,k)
    L2 = multikeyQS(S2,k+1)
    L3 = multikeyQS(S3,k)
    return L1+L2+L3
```
---

# Il Problema dello Zaino

---
# Esercizi

> 
