from suffixarray import buildSA

# Simple function calculating LCP of two string
def lcp(x, y):
    for i in range(min(len(x), len(y))):
        if x[i] != y[i]: return i
    return min(len(x), len(y))

# Naive way to calculate LCP array given string and its suffix array
def buildLCP(t, sa):
    lcparray= []
    for i in range(len(sa)-1):
       lcparray.append(lcp(t[sa[i]:], t[sa[i+1]:]))
    return lcparray
    #return [ lcp(t[sa[i]:], t[sa[i+1]:]) for i in xrange(len(sa)-1) ]


if __name__ == "__main__":
    T = 'mississippi$'
    print(buildLCP(T, buildSA(T))) # [0, 1, 1, 3, 0, 2]