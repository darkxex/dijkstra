import sys
import os
import copy



print ("Presiona 1 para cargar algoritmo de Color")
print ("Presiona 2 para cargar algoritmo de Dikstra")
x = input()
if (x == 1):
    print ("Algoritmo de Coloracion")
    os.system("color_navaja.py")
if (x == 2):
    print ("Algoritmo de Dijkstra")
    os.system("dijkstra.py")
