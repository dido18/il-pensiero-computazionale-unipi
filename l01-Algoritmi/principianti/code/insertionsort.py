

def insertionSort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key: # rispetto allo pseudocodice gli indici partono da 0
            A[i+1]=A[i]
            i = i - 1

        A[i+1] = key


if __name__ == "__main__":
    unaLista = [54,26,93,17,77,31,44,55,20]
    insertionSort(unaLista)
    print(unaLista)


