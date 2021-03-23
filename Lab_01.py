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
           
cc=int(input("Choose the number of cards (minimum 2): "))
cartas_totales=cc*2
tablero_respuestas=generarjuego(cc)
# print(tablero_respuestas)   #sacar print
print()

P1=0
P2=0

tablero_vacio=[]

for i in range(cartas_totales):
    tablero_vacio.append(0)
    

print(tablero_vacio)
print()

while P1+P2<cc:
    # TURNO JUGADOR 1
    print("~~~~Player1's turn~~~~")
    coordenada1=int(input('Choose a coordinate: '))
    tablero_vacio[coordenada1]=tablero_respuestas[coordenada1]
    print(tablero_vacio)
    coordenada2=int(input('Choose a coordinate: '))
    tablero_vacio[coordenada2]=tablero_respuestas[coordenada2]
    print(tablero_vacio)
    
    if tablero_respuestas[coordenada1]!=tablero_respuestas[coordenada2]:
        print("Fail")
        tablero_vacio[coordenada1]=0
        tablero_vacio[coordenada2]=0
    else:
        print("Nice!")
        P1+=1
        
    print() 
    print(tablero_vacio)
    print()
    
    #TURNO JUGADOR 2
    print("~~~~Player2's turn~~~~")
    coordenada1=int(input('Choose a coordinate: '))
    tablero_vacio[coordenada1]=tablero_respuestas[coordenada1]
    print(tablero_vacio)
    coordenada2=int(input('Choose a coordinate: '))
    tablero_vacio[coordenada2]=tablero_respuestas[coordenada2]
    print(tablero_vacio)
    
    if tablero_respuestas[coordenada1]!=tablero_respuestas[coordenada2]:
        print("Fail")
        tablero_vacio[coordenada1]=0
        tablero_vacio[coordenada2]=0
    else:
        print("Nice!")
        P2+=1

print()
if P1>P2:
    print("$$$$$Pleyer1 wins!$$$$$")
elif P1<P2:
    print("$$$$$Player2 wins!$$$$$")
else:
    print("It's a tie")