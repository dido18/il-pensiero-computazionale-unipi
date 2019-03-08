<!-- $size: 16:9 -->
<!-- page_number: true -->

Laboratorio di motori di ricerca 
===
<center>
	<img src=./img/copertina.jpg width="500">
</center>

---
# Costruzione SA (codice v1)
```python
# Not a great way to build a suffix array, it use quadratic space
def naiveBuildSA(text):
    # list of tuple (suffix,  index)
    satups = sorted([(text[i:], i) for i in range(len(text))]) 
    return list(map(lambda x: x[1], satups))
```

Complessità:
- Tempo: $O(n)$
- Spazio: $O(n^2)$ 

---
# Costruzione SA (codice v2)
La funzione ```suffixCmp``` viene usata dalla funzione ```sorted``` ritorna il suffisso nel testao da confrontare

```python
def buildSA(text):
    SA = [x for x in range(len(text))]
    # funzione di comparazione
    def suffixCmp(suffixPos):
        return text[suffixPos:]
    return sorted(SA, key=suffixCmp)
```

Complessità:
- Tempo: $O(n)$
- Spazio: $O(n)$ 

---
# Costruzione SA

```python
   T = 'mississippi$' # input("Inserisci testo")
    print(naiveBuildSA(T))
    print(buildSA(T))
