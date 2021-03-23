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
           
        
def generar_matriz(n):
    matriz = []
    for i in range(n):
        lista = [0]*n
        matriz.append(lista)
    return matriz
 
def imprime_matriz(matriz):
    for fila in matriz:
        var = ""
        for elemento in fila:
            var+= str(elemento) + " "
        print(var)

# n = int(input("tamaño matriz"))
# imprime_matriz(generar_matriz(n)) 


cc=int(input("Choose the number of cards: "))
print(generarjuego(cc))

P1=0
P0=0

print('Player 1 starts playing.')


