<!-- $size: 16:9 -->
<!-- page_number: true -->
Laboratorio di Motori di Ricerca
===
<center>
	<img src=./img/copertina.jpg width="400">
</center>

##### [Il Pensiero Computazionale](http://ilpensierocomputazionale.di.unipi.it/)
###### Percorso Formativo per i Docenti della Scuola Secondaria di II Grado
#### Lezione 4 (Parte pratica)
<sub><sup>Prof. [Paolo Ferragina](http://pages.di.unipi.it/ferragina/) and  [Davide Neri](http://pages.di.unipi.it/neri/)</sup></sub>




---
# Cosa faremo oggi
 
 - Costruzione SA (Suffix Array)
 - Ricerca di sottostringhe (Ricerca binaria in SA)
 - Costruzione LCP-array (Longest-Common-Prefix)


---
# Costruzione SA (pseudo-codice)
<center>
	<img src=./img/sa.jpg width="1000">
</center>

```Suffix_cmp()``` è la funzione in C-style usata per comparare due suffissi nella funzione  ```QSORT()``` 

<center>
	<img src=./img/suffix-cmp.JPG width="800">
</center>


---
# Costruzione SA (codice v1)

```python
def naiveBuildSA(text):
    # list of tuple (suffix,  index)
    satups = sorted([(text[i:], i) for i in range(len(text))]) 
    return list(map(lambda x: x[1], satups))
```

Complessità :
- Spazio: $O(n^2)$  
- Tempo: $O(n^2 \ log\ n)$

---
# Costruzione SA (codice v2)

la funzione ```suffixCmp()``` definisce  la funzione  per ordinare i suffissi in  ```sorted()```.

```python
def buildSA(text):
    # inizializza il SA con gli indici da [0, n-1]
    SA = [x for x in range(len(text))]
    # funzione di comparazione
    def suffixCmp(suffixPos):
        return text[suffixPos:]
    return sorted(SA, key=suffixCmp)
```

Complessità:
- Spazio: $O(n)$ 
- Tempo: $O(n^2 \ log\ n)$


---
# Costruzione SA (esempio)


```python
T = 'mississippi$' # input("Inserisci testo")

print(naiveBuildSA(T))
print(buildSA(T))

```
---
# Ricerca di sottostringhe 
Esempio di ricerca binaria della posizione in SA del pattern ```P = ssi``` all'interno della stringa ```mississippi$```.

<center>
	<img src=./img/substringsearch-example.jpg width="1000">
</center>

---
# Ricerca di sottostringhe con SA  (pseudo-codice)
<center>
	<img src=./img/substringsearch.JPG width="1000">
</center>

---
# Ricerca di sottostringhe con SA  (codice)

```python
def substringSearch(t, sa, p):
    assert t[-1] == '$'      # se t ha il terminatore
    assert len(t) == len(sa) # sa è il sa di t
    if len(t) == 1: return 1 # 

    n = len(sa) 
    l, r = 0, n-1

    while l != r: 
        m = int(math.floor((l + r) / 2))
        suffixM = t[sa[m]:]
        if p > suffixM:
            l = m + 1
        else:
            r = m
    suffixL = t[sa[l]:] 
    if suffixL.startswith(p):
        return l
    else:
        return None
```
---
# Ricerca di sottostringhe con SA  (esempio)

```python
T = 'mississippi$' 
SA = buildSA(T)

P = "ssi"
isa = substringSearch(T, SA, P)
if isa is None:
    print("Substring ", P, " not found")
else:
    print("Substring ", P, " found in" , T[SA[isa]:])
    
P = "ti"
isa = substringSearch(T, SA, P)
if isa is None:
    print("Substring ", P, " not found")
else:
    print("Substring ", P, " found in" , T[SA[isa]:])
```

---
# Costruzione LCP (codice v1)
```python
# Calcola il lcp tra due stringhe
def lcp(x, y):
    for i in range(min(len(x), len(y))):
        if x[i] != y[i]: return i
    return min(len(x), len(y))

def naiveBuildLCP(t, sa):
    lcparray= []
    for i in range(len(sa)-1):
        nlcp = lcp(t[sa[i]:], t[sa[i+1]:])
        lcparray.append(nlcp)
    return lcparray
```

---
# Costruzione LCP - kasai's algorithm (pseudo-codice)
<center>
	<img src=./img/lcp-build.JPG width="600">
</center> 

Complessità:
- Tempo: $O(n)$
- Spazio: $O(n)$

---
# Costruzione LCP - Kasai's algorithm (codice v2)
```python
def buildLCP(t, sa):
    # sa_inverse = per ogni suffisso ritorna la posizione in SA
    sa_inverse = [0 for i in range(len(t))]
    for i in range(len(t)):
        sa_inverse[sa[i]] = i 
        
    h = 0
    lcp = [0 for i in range(len(sa)-1)]
    for i in range(len(t)):
        q = sa_inverse[i]
        if q > 1:
            k = sa[q-1]
            if (h > 0):
                h -=1
            while T[k + h] == T[i+h]:
                h += 1
            lcp[q-1] = h
    return lcp
```

---
# Costruzione LCP (esempio)
```python
T = 'mississippi$'
SA = buildSA(T)
  
print(naiveBuildLCP(T, SA)) 
print(buildLCP(T, SA))
 ```
