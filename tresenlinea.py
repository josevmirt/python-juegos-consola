from random import randrange
def DisplayBoard(board):
    dis=len(MakeListOfFreeFields(board))
    print("+-------+-------+-------+",sep="")
    print("|       |       |       |",sep="")
    print("|   ",board[0][0],"   |   ",board[0][1],"   |   ",board[0][2],"   |",sep="")
    print("|       |       |       |",sep="")
    print("+-------+-------+-------+",sep="")
    print("|       |       |       |",sep="")
    print("|   ",board[1][0],"   |   ",board[1][1],"   |   ",board[1][2],"   |",sep="")
    print("|       |       |       |",sep="")
    print("+-------+-------+-------+",sep="")
    print("|       |       |       |",sep="")
    print("|   ",board[2][0],"   |   ",board[2][1],"   |   ",board[2][2],"   |",sep="")
    print("|       |       |       |",sep="")
    print("+-------+-------+-------+",sep="")
     
def EnterMove(board):
    dis=MakeListOfFreeFields(board)
    lst=[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    while True:
        try:
            move=int(input("Ingresa tu movimiento: "))
            if move >0 and move <10:
                move=lst[move-1]
                if move in dis:
                    board[move[0]][move[1]]="O"
                    break
                else:
                    print("Ocupado")
            else:
                print("Numero invalido")
             
        except:
            print("Debe ingresar un numero entero")

    return board

def MakeListOfFreeFields(board):
    lis=[]
    for i in range(3):
        for j in range(3):
            if not (tablero[i][j]=="X" or tablero[i][j]=="O"):
                lis.append((i,j))
    return lis

def VictoryFor(board, sign):
    win=False
    for i in range(3):
        if board[i]==[sign,sign,sign]:
            win=True
        elif [board[0][i],board[1][i],board[2][i]]==[sign,sign,sign]:
            win=True
    if [board[0][0],board[2][2],board[1][1]]==[sign,sign,sign]or\
       [board[0][2],board[2][0],board[1][1]]==[sign,sign,sign]:
        win=True
    if win and sign=="O":
        print ("¡Has Ganado!")
        return True
    elif win and sign=="X":
        print ("¡La Comutadora ha Ganado!")
        return True
    return False
    
def DrawMove(board):
    dis=MakeListOfFreeFields(board)
    lst=[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    while True:
        move=randrange(9)
        move=lst[move-1]
        if move in dis:
            board[move[0]][move[1]]="X"
            break
    return board

tablero=[[1,2,3],[4,"X",6],[7,8,9]]
turn=1
DisplayBoard(tablero)
while True:
    if turn%2:
        tablero=EnterMove(tablero)
        turn+=1
        DisplayBoard(tablero)
        if VictoryFor(tablero, "O"):
            break
    else:
        tablero=DrawMove(tablero)
        turn+=1
        DisplayBoard(tablero)
        if VictoryFor(tablero, "X"):
            break
    if len(MakeListOfFreeFields(tablero))==0:
        print("Empate")
        break
print("Gracias por Jugar")  
        


