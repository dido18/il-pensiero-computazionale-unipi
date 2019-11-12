def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:
       splitpoint = partition(alist,first,last)
       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)

def partition(alist, firt, last):
    pivot = alist[last]
    i = firt - 1
    for j in range(firt, last):
        if alist[j] <= pivot:
            i = i + 1
            swap(alist, i, j)
    swap(alist, i + 1, last)
    return i + 1

def swap(alist, i, j):
    temp = alist[i]
    alist[i] = alist[j]
    alist[j] = temp

if __name__ == "__main__":
    alist = [54,26,93,17,77,31,44,55,20]
    quickSort(alist)
    print(alist)