colores = ['Rojo', 'Azul', 'Verde', 'Amarillo', 'Morado']

nodos = []

adyecentes = {}


colores_of_nodos = {}

def promising(state, color):
    for neighbor in adyecentes.get(state): 
        color_vecino = colores_of_nodos.get(neighbor)
        if color_vecino == color:
            return False

    return True

def get_color_for_state(state):
    for color in colores:
        if promising(state, color):
            return color

def main():
    limit = input("Ingrese cantidad de Nodos: ")
    for x in range(0, limit ):
        nodos.append(str(x))
        ex = raw_input("Ingrese Nodos adyecentes para el Nodo " + str(x) + "(Ej. 1,2):" )
        adyecentes[str(x)] = ex.split(",")
  
    for state in nodos:
        colores_of_nodos[state] = get_color_for_state(state)
    
    print colores_of_nodos


main()
