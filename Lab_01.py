from numpy import *
from numpy import random

def generarjuego(m):   # m=número de cartas
    tablero=[]

    for i in range(2):
        numeros=[]
        for i in range(1,m+1):
                numeros.append(i)    
        random.shuffle(numeros)
        tablero.append(numeros)
    
    tablero_real=[]
    for i in range(2):
        for j in range(m):
            tablero_real.append(tablero[i][j])
    return tablero_real
           
# def generar_tablero(n):
#     matriz = []
#     for i in range(n):
#         lista = [0]*n
#         matriz.append(lista)
#     return matriz
 
# def imprime_tablero(matriz):
#     for fila in matriz:
#         var = ""
#         for elemento in fila:
#             var+= str(elemento) + " "
#         print(var)

# n = int(input("tamaño tablero"))
# imprime_matriz(generar_matriz(n)) 


cc=int(input("Choose the number of cards: "))
cartas_totales=cc*2
tablero_respuestas=generarjuego(cc)
print(tablero_respuestas)   #sacar print
print()

P1=0
P2=0

tablero_vacio=[]

for i in range(cartas_totales):
    tablero_vacio.append(0)
    
print("Player 1 starts playing.")
print(tablero_vacio)


while P1+P2<cc:
    # TURNO JUGADOR 1
    coordenada1_P1=int(input('Choose a coordinate: '))
    
    
    coordenada2_P1=int(input('Choose a coordinate: '))
    
    print()
    print(coordenada1_P1)
    print(coordenada2_P1)   
    break
