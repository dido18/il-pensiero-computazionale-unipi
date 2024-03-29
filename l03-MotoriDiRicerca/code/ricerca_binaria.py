import math
from suffixarray import buildSA


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

    #print(binarysearchSAWhile(T, SA,P))
