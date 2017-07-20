colors = ['Rojo', 'Blanco', 'Verde', 'Azul', 'Amarillo']

states2 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n"]
states = []

neighbors = {}
neighbors['a'] = []
neighbors['b'] = []
neighbors['c'] = []
neighbors['d'] = []
neighbors['e'] = []
neighbors['f'] = []
neighbors['g'] = []
neighbors['h'] = []
neighbors['i'] = []
neighbors['j'] = []
neighbors['k'] = []
neighbors['l'] = []
neighbors['m'] = []
neighbors['n'] = []


colors_of_states = {}

def promising(state, color):
    for neighbor in neighbors.get(state): 
        color_of_neighbor = colors_of_states.get(neighbor)
        if color_of_neighbor == color:
            return False

    return True

def get_color_for_state(state):
    for color in colors:
        if promising(state, color):
            return color

def main():
    estados=input("   Ingrese la cantidad de estados : ")
    for i in range(estados):
        states.append(states2[i])
        ##print states[i]
        
    for j in range(estados):
        for k in range(estados):
            c="no"
            if((states[j]!=states[k])):
                c=raw_input("El estado '"+ states[j] + "' es vecino del estado '"+ states[k] +"' : ")
            if (c=="si"):
                neighbors[states[j]].append(states[k])
            ##print neighbors[states[j]]
    contador0=0
    contador1=0
    contador2=0
    contador3=0
    contador4=0
        
    for state in states:
        colors_of_states[state] = get_color_for_state(state)
        if (colors_of_states[state]=='Rojo'):
            contador0=contador0+1
        if (colors_of_states[state]=='Blanco'):
            contador1=contador1+1
        if (colors_of_states[state]=='Verde'):
            contador2=contador2+1
        if (colors_of_states[state]=='Azul'):
            contador3=contador3+1
        if (colors_of_states[state]=='Amarillo'):
            contador4=contador4+1

    cantidaddecolor = 0
    if contador0 > 0:
        cantidaddecolor = cantidaddecolor+1
    if contador1 > 0:
        cantidaddecolor = cantidaddecolor+1
    if contador2 > 0:
        cantidaddecolor = cantidaddecolor+1
    if contador3 > 0:
        cantidaddecolor = cantidaddecolor+1
    if contador4 > 0:
        cantidaddecolor = cantidaddecolor+1

    print "Colores necesarios: " + str(cantidaddecolor)
    print colors_of_states
    if(contador0>contador1):
        if(contador0>contador2):
            if(contador0>contador3):
                if(contador0>contador4):
                    print "EL color Rojo fue el mas usado con : "+ str(contador0)
                else:
                    print "EL color Amarillo fue el mas usado con : "+ str(contador4)
            else:
                if(contador3>contador4):
                    print "EL color Azul fue el mas usado con : "+ str(contador3)
                else:
                    print "EL color Amarillo fue el mas usado con : "+ str(contador4)
        else:
            if(contador2>contador3):
                if(contador2>contador4):
                    print "EL color Verde fue el mas usado con : "+ str(contador2)
                else:
                    print "EL color Amarillo fue el mas usado con : "+ str(contador4)
            else:
                if(contador3>contador4):
                    print "EL color Azul fue el mas usado con : "+ str(contador3)
                else:
                    print "EL color Amarillo fue el mas usado con : "+ str(contador4)
    else:
        if(contador1>contador2):
            if(contador1>contador3):
                if(contador1>contador4):
                    print "EL color Blanco fue el mas usado con : "+ str(contador1)
                else:
                    print "EL color Amarillo fue el mas usado con : "+ str(contador4)
            else:
                if(contador3>contador4):
                    print "EL color Azul fue el mas usado con : "+ str(contador3)
                else:
                    print "EL color Amarillo fue el mas usado con : "+ str(contador4)
        else:
            if(contador2>contador3):
                if(contador2>contador4):
                    print "EL color Verde fue el mas usado con : "+ str(contador2)
                else:
                    print "EL color Amarillo fue el mas usado con : "+ str(contador4)
            else:
                if(contador3>contador4):
                    print "EL color Azul fue el mas usado con : "+ str(contador3)
                else:
                    print "EL color Amarillo fue el mas usado con : "+ str(contador4)
        
    


main()
cerrar = raw_input()
