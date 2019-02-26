import time

from lineare import lineare
from quadratico import quadratico
from cubico import cubico

d = [10, +4, -6, +3, +1, +3, -2, +3, -4, +1, -9, +6]


start = time.time() # segna il tempo di inizio nella variabile start
cubico(d)
stop = time.time() # segna il tempo di fine nella variabile start
print('Cubico ', stop-start, "secondi.")

start = time.time() # segna il tempo di inizio nella variabile start
quadratico(d)
stop = time.time() # segna il tempo di fine nella variabile start
print('Quadratico ', stop-start, "secondi.")


start = time.time() # segna il tempo di inizio nella variabile start
lineare(d)
stop = time.time() # segna il tempo di fine nella variabile start
print('Lineare ', stop-start, "secondi.")


