import math
from suffixarray import buildSA


def substringSearch(t, sa, p):
    assert t[-1] == '$'      # se t ha il terminatore
    assert len(t) == len(sa) # sa è il sa di t
    if len(t) == 1: return 1
 
    # invariant: sa[l] < p < sa[r]
    n = len(sa) 
    l = 0
    r = n - 1

    while l != r : #<= r: # l <= j:
        # math.floor() restituisce l'intero <= x piu' vicino a x
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
        return -1

def binarysearchSA(t, sa, p):
    assert t[-1] == '$'     # t ha il terminatore
    assert len(t) == len(sa) # sa è il sa dl t
    if len(t) == 1: return 1
   
    #l, r = 0, len(sa) # invariant: sa[l] < p < sa[r]
    n = len(sa) 

    i = 0
    j = n - 1

    while i <= j: # i <= j:
        # math.floor() restituisce l'intero <= x piu' vicino a x
        # int() rimuove la virgola
        # m e' la posizione centrale tra i e j

        m = int(math.floor((i + j) / 2))

        suffix = t[sa[m]:]
        if p < suffix:
            j = m - 1
        if p > suffix:
            i = m + 1
    return i

def binarysearchSAWhile(t, sa, p):
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
    T = 'mississippi$' 

    SA = buildSA(T)
    P = "ssi"
    i1 = binarysearchSA(T, SA, P)
    i2 = binarysearchSAWhile(T, SA, P)
    i3 = substringSearch(T, SA, P)
    
    print(i1,i2,i3)
    print(T[SA[i1]:])
    print(T[SA[i2]:])
    print(T[SA[i3]:])

    # print(binarysearchSA(T, SA, "mis"))
    # print(binarysearchSAWhile(T, SA, "mis"))

    # print(binarysearchSA(T, SA, "ssippi"))
    # print(binarysearchSAWhile(T, SA, "ssippi"))

    # print(binarysearchSA(T, SA, "tt"))
    # print(binarysearchSAWhile(T, SA, "t"))

    # print(binarysearchSA(T, SA, "pi"))
    # print(binarysearchSAWhile(T, SA, "pi"))


    # t = 'abaaba$'
    # sa = buildSA(t)
    # print(binarysearchSA(t, sa, 'aba'))
    # print(binarysearchSA2(t, sa, 'aba'))

    # print(binarysearchSA(t, sa, 'bb'))
    # print(binarysearchSA2(t, sa, 'bb'))

    # print(binarysearchSA(t, sa, 'aa'))
    # print(binarysearchSA2(t, sa, 'aa'))






# def ricerca_binaria(insieme, dato):
#     """
#     Ricerca binaria di un elemento dato in insieme
#     :param insieme: insieme su cui ricercare (ordinato)
#     :param dato: dato da ricercare
#     """

#     # n indica il numero di elementi di insieme
#     n = len(insieme)

#     i = 0
#     j = n - 1

#     while i <= j:
#         # math.floor() restituisce l'intero <= x piu' vicino a x
#         # int() rimuove la virgola
#         # m e' la posizione centrale tra i e j

#         m = int(math.floor((i + j) / 2))

#         if dato == insieme[m]:
#             print ("{} e' presente".format(dato))
#             return
#         if dato < insieme[m]:
#             j = m - 1
#         if insieme[m] < dato:
#             i = m + 1

#     print ("{} non e' presente".format(dato))
