from numpy import *
from numpy import random

def generategame(m):   # m=number of cards (this function creates and randomizes the ammount of numbers)
    table=[]

    for i in range(2):
        numbers=[]
        for i in range(1,m+1):
                numbers.append(i)    
        random.shuffle(numbers)
        table.append(numbers)
    
    table_real=[]
    for i in range(2):
        for j in range(m):
            table_real.append(table[i][j])
    return table_real
           
cc=int(input("Choose the number of cards (minimum 2): "))     #we ask the players the ammount of cards
total_cards=cc*2
table_answers=generategame(cc)          #we create the answers for th game to check them later
print()

P1=0
P2=0        #we set the initial scores

table_close=[]

for i in range(total_cards):
    table_close.append(0)           #we create a blank game table
    

print(table_close)
print()

while P1+P2<cc:                                 #starts the game
    # PLAYER1'S TURN
    print("~~~~Player1's turn~~~~")
    coord1=int(input('Choose a coordinate: '))
    table_close[coord1]=table_answers[coord1]
    print(table_close)
    coord2=int(input('Choose a coordinate: '))
    table_close[coord2]=table_answers[coord2]
    print(table_close)
    
    if table_answers[coord1]!=table_answers[coord2]:
        print("Fail")
        table_close[coord1]=0
        table_close[coord2]=0
    else:
        print("Nice!")
        P1+=1
        table_close.pop(coord1)
        table_close.insert(coord1,'*')
        
        table_close.pop(coord2)
        table_close.insert(coord2,'*')
      
        table_answers.pop(coord1)
        table_answers.insert(coord1,'*')
       
        table_answers.pop(coord2)
        table_answers.insert(coord2,'*')
        
        
    print() 
    print(table_close)
    print()
    
    #PLAYER2'S TURN
    print("~~~~Player2's turn~~~~")
    coord1=int(input('Choose a coordinate: '))
    table_close[coord1]=table_answers[coord1]
    print(table_close)
    coord2=int(input('Choose a coordinate: '))
    table_close[coord2]=table_answers[coord2]
    print(table_close)
    
    if table_answers[coord1]!=table_answers[coord2]:
        print("Fail")
        table_close[coord1]=0
        table_close[coord2]=0
    else:
        print("Nice!")
        P2+=1
        table_close.pop(coord1)
        table_close.insert(coord1,'*')
        
        table_close.pop(coord2)
        table_close.insert(coord2,'*')
      
        table_answers.pop(coord1)
        table_answers.insert(coord1,'*')
       
        table_answers.pop(coord2)
        table_answers.insert(coord2,'*')

    print() 
    print(table_close)
    print()

print()
if P1>P2:
    print("$$$$$Pleyer1 wins!$$$$$")
elif P1<P2:
    print("$$$$$Player2 wins!$$$$$")
else:
    print("It's a tie")