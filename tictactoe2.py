

import time
m=input("enter player1 name:")
n=input("enter player2 name:")
print(m,"your icon is X")
print(n,"your icon is 0")
time.sleep(1)
print("\t\t\thello " ,m, "," ,n, "welcome to tic tac toe game")
time.sleep(1)

def sum(a,b,c):
    return a+b+c

def printboard(xstate,zstate):
    one="x" if xstate[1] else ("0" if zstate[1] else 1)
    two="x" if xstate[2] else ("0" if zstate[2] else 2)
    three="x" if xstate[3] else ("0" if zstate[3] else 3)
    four="x" if xstate[4] else ("0" if zstate[4] else 4)
    five="x" if xstate[5] else ("0" if zstate[5] else 5)
    six="x" if xstate[6] else ("0" if zstate[6] else 6)
    seven="x" if xstate[7] else ("0" if zstate[7] else 7)
    eight="x" if xstate[8] else ("0" if zstate[8] else 8)
    nine="x" if xstate[9] else ("0" if zstate[9] else 9)
    print(f"\t\t\t\t {one} | {two} | {three} ")
    print(f"\t\t\t\t---|---|---")
    print(f"\t\t\t\t {four} | {five} | {six} ")
    print(f"\t\t\t\t---|---|---")
    print(f"\t\t\t\t {seven} | {eight} | {nine} ")


def checkwin(xstate,zstate):
    wins=[[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7],[3,6,9],[1,4,7],[2,5,8]]
    for win in wins:
        if (sum(xstate[win[0]],xstate[win[1]],xstate[win[2]])==3):
            printboard(xstate,zstate)
            print("\t\t\t\t Congratulations" ,m, "you wons the match")
            return 1
        
        if (sum(zstate[win[0]],zstate[win[1]],zstate[win[2]])==3):
            printboard(xstate,zstate)
            print("\t\t\t\tCongratulation" ,n, "you wons the match")
            return 0
    return -1
    
if __name__=="__main__":
    xstate=[0,0,0,0,0,0,0,0,0,0]
    zstate=[0,0,0,0,0,0,0,0,0,0]
    turn=1
    print("\t\t\t\tlet's start the game")
    w=0
    while (True):
        w=w+1
        if w<10:
            printboard(xstate,zstate)
            if turn==1:
                print("\t\t\t\t" ,m, "chance")
                value = int(input("enter a value:"))
                xstate[value]=1
            else:
                print("\t\t\t\t" ,n, "chance")
                value = int(input("enter a value:"))
                zstate[value]=1
        else:
            printboard(xstate,zstate)
            print("\t\t\t\tmatch draw")
            break

        cwin=checkwin(xstate,zstate)
        if(cwin!=-1):
            print("\t\t\t\tmatch over")
            break
        turn=1-turn
