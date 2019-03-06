

# Not a great way to build a suffix array, it use quadratic space
def naiveBuildSA(text):
    satups = sorted([(text[i:], i) for i in range(len(text))]) # list of tuple (suffix,  index)
    return list(map(lambda x: x[1], satups))

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
    