

# Not a great way to build a suffix array, it use quadratic space
def naiveBuildSA(text):
    suff_ind = []  # list of tuple (suffix, index)
    for i in range(len(text)):
        t = (text[i:], i)
        suff_ind.append(t)
    suff_ind.sort()   
    sa = []
    for (_, index) in suff_ind:
        sa.append(index)
    return sa 
    #satups = sorted([(text[i:], i) for i in range(len(text))]) 
    #return list(map(lambda x: x[1], satups))

def buildSA(text):
    SA = [x for x in range(len(text))]
    # funzione di comparazione
    def suffixCmp(suffixPos):
        return text[suffixPos:]
    return sorted(SA, key=suffixCmp)

if __name__ == "__main__":
    T = 'mississippi$' # input("Inserisci testo")
    print(naiveBuildSA(T))
    print(buildSA(T))
    