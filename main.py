import random
from queue import Queue
class Proces:
    def __init__(self,id, arrive, burst):
        self.id=id
        self.arrive = arrive
        self.burst = burst
    def printeaza(self):
        print("P", self.id, " arrive at:", self.arrive, "and needs", self.burst)
    def scadere (self, q):
        self.burst=self.burst-q
coada = Queue()
id=1
timp = int(input("Timpul este: "))
q = int(input("Cuanta este"))
procesor = Proces(0,0,0)
maxima=0
suma=0
lista = []
lista.append(Proces(id,random.randint(1, 20), random.randint(5, 20)))
#lista[0].printeaza()
i=1
for cronometru in range (0, timp):
    if cronometru == lista[i-1].arrive :
            lista.append(Proces(lista[i-1].id + 1,lista[i-1].arrive + random.randint(1, 20), random.randint(5, 20)))
            #lista[i].printeaza()
            i=i+1
g=0
for cronometru in range (0, timp):
    if cronometru == lista[g].arrive :
        coada.put(lista[g])
        g=g+1
    suma=suma+coada.qsize()
    if coada.empty() == False:
        if procesor:
            if procesor.burst < q:
                cronometru=cronometru+procesor.burst
                procesor.burst=0
                procesor.printeaza()
                procesor= coada.get()
            if cronometru % q == 0 :
                procesor.scadere(q)
                if procesor.burst > 0:
                    coada.put(procesor)
                if coada.qsize() > maxima:
                    maxima=coada.qsize()
                procesor = coada.get()
                procesor.printeaza()
            if cronometru % q == procesor.burst:
                procesor.scadere(procesor.burst)
        else:
            if cronometru % q == 0:
                procesor = coada.get()
print("Dimensiunea maxima este")
print(maxima)
print("Dimensiunea medie este")
print(suma/timp)






