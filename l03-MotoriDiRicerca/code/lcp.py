from suffixarray import buildSA


# Simple function calculating LCP of two string
def lcp(x, y):
    for i in range(min(len(x), len(y))):
        if x[i] != y[i]: return i
    return min(len(x), len(y))

# Naive way to calculate LCP array given string and its suffix array
def naiveBuildLCP(t, sa):
    lcparray= []
    for i in range(len(sa)-1):
        nlcp = lcp(t[sa[i]:], t[sa[i+1]:])
        lcparray.append(nlcp)
    return lcparray


def buildLCP(t, sa):
    ''' Kasai's algorithm to construct the lcp with O(n) space.
    '''
    sa_inverse = [0 for i in range(len(t))]
    for i in range(len(t)):
        sa_inverse[sa[i]] = i 
    h = 0
    lcp = [0 for i in range(len(sa)-1)]
    for i in range(len(t)):
        # sa-1 = returns for every suffix its position in SA
        q = sa_inverse[i]
        if q > 1:
            k = sa[q-1]
            if (h > 0):
                
                h -=1
            while T[k + h] == T[i+h]:
                h += 1
            lcp[q-1] = h
    return lcp

if __name__ == "__main__":
    T = 'mississippi$'
    SA = buildSA(T)
    print(naiveBuildLCP(T, SA)) 
    print(buildLCP(T, SA))