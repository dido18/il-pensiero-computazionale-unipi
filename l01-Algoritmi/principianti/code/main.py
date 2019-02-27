import random as rnd
import time

from insertionsort import insertionSort
from quicksort import  quickSort 

num_elements = 10000   # lunghezza della lista da ordinare

unaLista = []
# generiamo una lista di 10000 interi a caso 
for i in range(num_elements):
   unaLista.append(rnd.randint(1,100000))
    
start = time.time() # segna il tempo di inizio nella variabile start
insertionSort(unaLista)
stop = time.time() # segna il tempo di fine nella variabile start
print('Insertion sort per', stop-start, "secondi.")

unaLista = []
for i in range(num_elements):
   unaLista.append(rnd.randint(1,100000))
   
start = time.time() # segna il tempo di inizio nella variabile start
quickSort(unaLista)
stop = time.time() # segna il tempo di fine nella variabile start
print('Quick Sort per', stop-start, "secondi.")

unaLista = []
for i in range(num_elements):
   unaLista.append(rnd.randint(1,100000))
   
start = time.time() # segna il tempo di inizio nella variabile start
sorted(unaLista)
stop = time.time() # segna il tempo di fine nella variabile start
print('Merge Sort per', stop-start, "secondi.")