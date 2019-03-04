# Soluzione in Python dalle olimpiadi di matematica (2015)

def trovaVittorie(numGraffette, numVittoria):      
   numGraffette = numGraffette + 1
   soluzione = [0] * numGraffette 
   soluzione[numVittoria] = 1

   for i in range(1, numGraffette):
      if (soluzione[i] == 1):
         solUno = i * 2 # un numero a cui applicare g
         solDue = i + 3 # un numero a cui applicare f
         if (solUno < 2015):
            soluzione[solUno] = 1
         if (solDue < 2015):
            soluzione[solDue] = 1
            
   return sum(soluzione)

print(trovaVittorie(2015, 3)) # soluzione di (a) = 671
print(trovaVittorie(2015, 1)) # soluzione di (b) = 1343

