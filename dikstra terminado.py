from collections import defaultdict
from heapq import *

def dijkstra(trans, f, t):
    g = defaultdict(list)
    for l,r,c in trans:
        g[l].append((c,r))

    q, seen = [(0,f,())], set()
    while q:
        (cost,v1,camino) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            camino = (v1, camino)
            if v1 == t: return (cost, camino)

            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost+c, v2, camino))

    return float("inf")

if __name__ == "__main__":
    trans = []
    print "Ingrese Matriz de Peso Ej. (Nodo,Nodo adyecente,Peso) o escriba fin para terminar ingreso."
    x = ""
    while(x != "fin"):    
     
        x = raw_input("(Nodo, Nodo adyecente, Peso)=")
        if (x != "fin"):
        
            a,b,c = x.split(",")
            c = int(c)
            trans.append((a, b, c))
  
        
    x = ""
    print "Transiciones:"
    print trans
    while(x != "fin"):    
        
    
        orig = raw_input("Ingrese Nodo Origen: ")
        fin = raw_input("Ingrese Nodo Destino: ")
        print "Distancia de " + orig + " a " + fin
        print dijkstra(trans,orig,fin)
        x = raw_input("escriba fin para terminar: ")

    
   
