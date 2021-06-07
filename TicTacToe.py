import random

#Function to print board
def prt(lst0):
    print('\n'*10)
    print(lst0[0],'   ',lst0[1],'   ',lst0[2])
    print()
    print(lst0[3],'   ',lst0[4],'   ',lst0[5])
    print()
    print(lst0[6],'   ',lst0[7],'   ',lst0[8])
    
    

#Function to check the winner
def chk_win(lstw):
    if((lstw[0]==lstw[1]==lstw[2]=="X")or(lstw[0]==lstw[1]==lstw[2]=="O")):
        print('\n'*2) 
        return 0
    elif((lstw[3]==lstw[4]==lstw[5]=="X")or(lstw[3]==lstw[4]==lstw[5]=="O")):
        print('\n'*2)
        return 0
    elif((lstw[6]==lstw[7]==lstw[8]=="X")or(lstw[6]==lstw[7]==lstw[8]=="O")):
        print('\n'*2)
        return 0
    elif((lstw[0]==lstw[3]==lstw[6]=="X")or(lstw[0]==lstw[3]==lstw[6]=="O")):
        print('\n'*2)
        return 0
    elif((lstw[1]==lstw[4]==lstw[7]=="X")or(lstw[1]==lstw[4]==lstw[7]=="O")):
        print('\n'*2)
        return 0
    elif((lstw[2]==lstw[5]==lstw[8]=="X")or(lstw[2]==lstw[5]==lstw[8]=="O")):
        print('\n'*2)
        return 0
    elif((lstw[0]==lstw[4]==lstw[8]=="X")or(lstw[0]==lstw[4]==lstw[8]=="O")):
        print('\n'*2)
        return 0
    elif((lstw[2]==lstw[4]==lstw[6]=="X")or(lstw[2]==lstw[4]==lstw[6]=="O")):
        print('\n'*2)
        return 0
    return 1



#Function to take input from player
def ply(lst1,y):
    print('\n'*5)
    x=int(input("Enter your position :"))
    if((x>9)and(x<0)):
        print("\t\t!!!!!")
        print("\tPlz enter a valid position")
        return ply(lst1,y)
    elif (lst1[x-1]=="."):
        lst1[x-1]=y
        return lst1
    else:
        print("\t\t!!!!!")
        print("\tPlz enter a valid position")
        return ply(lst1,y)






#Creating a list
def genlst():
    lstg=list()
    for i in range(11):
        lstg.append('.')
    return lstg



def mstart():
    l=random.randint(1,2)   #Generating random value to select player
    lst[9]=l 

#Taking Marker choice from PLAYERS
    if l==1: 
        print("\t\tPLAYER 1 goes FIRST:")
        h1=input("Choose Your Marker 'X' or 'O' :")
        if h1=='X':
            i1='O'
        else:
            i1='X'
    else:
        print("\t\tPLAYER 2 goes FIRST:")
        i1=input("Choose Your Marker 'X' or 'O' :")
        if i1=='X':
            h1='O'
        else:
            h1='X'
    return h1,i1
        

#HERE FUN BEGINS        

p=1
t=0
while(p==1):
    print('\n'*10)
    t=0
    lst=genlst()
    h,i=mstart()
    prt(lst)
    while t<9:
        w=chk_win(lst)
        if w==0:
            if(lst[9]==2):
                print("\t\tPLAYER 1 is WINS")
            else:
                print("\t\tPLAYER 2 is WINS")
            break;        
        if lst[9]==1:
             print()
             print("\t\tPlayer 1 TURN:")
             lst=ply(lst,h)
             lst[9]=2
        else:
            print()
            print("\t\tPlayer 2 TURN:")
            lst=ply(lst,i)
            lst[9]=1
        prt(lst)
        t+=1
    else:
        print("ROUND DRAW")
    p=int(input('''Enter your Choice:
                \tPress 1 to Play Again
                \tPress 2 to Exit  '''))
                
print("\t\t\t!!GAME OVER!!")