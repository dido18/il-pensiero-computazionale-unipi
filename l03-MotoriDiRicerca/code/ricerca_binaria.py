import math
from suffixarray import buildSA

def ricerca_binaria(insieme, dato):
    """
    Ricerca binaria di un elemento dato in insieme
    :param insieme: insieme su cui ricercare (ordinato)
    :param dato: dato da ricercare
    """

    # n indica il numero di elementi di insieme
    n = len(insieme)

    i = 0
    j = n - 1

    while i <= j:
        # math.floor() restituisce l'intero <= x piu' vicino a x
        # int() rimuove la virgola
        # m e' la posizione centrale tra i e j

        m = int(math.floor((i + j) / 2))

        if dato == insieme[m]:
            print ("{} e' presente".format(dato))
            return
        if dato < insieme[m]:
            j = m - 1
        if insieme[m] < dato:
            i = m + 1

    print ("{} non e' presente".format(dato))

def binarysearchSA(t, sa, p):
    assert t[-1] == '$'     # t ha il terminatore
    assert len(t) == len(sa) # sa è il sa di t
    if len(t) == 1: return 1
   
    #l, r = 0, len(sa) # invariant: sa[l] < p < sa[r]

     # n indica il numero di elementi di insieme
    n = len(sa) #len(insieme)

    i = 0
    j = n - 1

    while i <= j:
        # math.floor() restituisce l'intero <= x piu' vicino a x
        # int() rimuove la virgola
        # m e' la posizione centrale tra i e j

        #m = int(math.floor((i + j) / 2))
        m = (i + j) // 2

        suffix = t[sa[m]:]

        if p == suffix: # TODO: no exact match  ??? 
            #print ("{} e' presente".format(p))
            return m
        if p < suffix:
            j = m - 1
        if suffix < p:
            i = m + 1
    return None
    #print ("{} non e' presente".format(p))

def binarysearchSA2(t, sa, p):
    assert t[-1] == '$' # t already has terminator
    assert len(t) == len(sa) # sa is the suffix array for t
    if len(t) == 1: return 1
    l, r = 0, len(sa) # invariant: sa[l] < p < sa[r]
    while True:
        c = (l + r) // 2
        # determine whether p < T[sa[c]:] by doing comparisons
        # starting from left-hand sides of p and T[sa[c]:]
        plt = True # assume p < T[sa[c]:] until proven otherwise
        i = 0
        while i < len(p) and sa[c]+i < len(t):
            if p[i] < t[sa[c]+i]:
                break # p < T[sa[c]:]
            elif p[i] > t[sa[c]+i]:
                plt = False
                break # p > T[sa[c]:]
            i += 1 # tied so far
        if plt:
            if c == l + 1: return c
            r = c
        else:
            if c == r - 1: return r
            l = c
if __name__ == "__main__":
    # T = 'mississippi$' # input("Inserisci testo")
    # pattern = "ss"
    # SA = buildSA(T)
    # binarysearchSA(T, SA, pattern )
    t = 'abaaba$'
    sa = buildSA(t)
    print(binarysearchSA(t, sa, 'aba$'))
    print(binarysearchSA2(t, sa, 'aba$'))

    print(binarysearchSA(t, sa, 'bb$'))
    print(binarysearchSA2(t, sa, 'bb$'))

    print(binarysearchSA(t, sa, 'aa'))
    print(binarysearchSA2(t, sa, 'aa'))





