import time
import random
from lineare import lineare
from quadratico import quadratico
from cubico import cubico

giorni = 5000 # number of days (length of d array)
d = [random.randrange(-10,10) for num in range(giorni)]

start = time.time() 
cubico(d)
stop = time.time() 
print('Cubico ', stop-start, "secondi.")

start = time.time() 
quadratico(d)
stop = time.time() 
print('Quadratico ', stop-start, "secondi.")

start = time.time() 
lineare(d)
stop = time.time() 
print('Lineare ', stop-start, "secondi.")


