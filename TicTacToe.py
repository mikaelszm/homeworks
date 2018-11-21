import os
tableau = [1,2,3,4,5,6,7,8,9]

def show():
     print("|",tableau[0],"|",tableau[1],"|",tableau[2],"|")
     print("-------------")
     print("|",tableau[3],"|",tableau[4],"|",tableau[5],"|")
     print("-------------")
     print("|",tableau[6],"|",tableau[7],"|",tableau[8],"|")
     print("-------------")
show()
i=0
def replay():
    decision = input("Do you want to play again????(Y?/N)")
    if decision.upper() == 'Y':
        return True
    else:
        return False
def checkAll(char):
        if checkLine(char,0,1,2):
            return True
        elif checkLine(char,3,4,5):
            return True
        elif checkLine(char,6,7,8):
            return True
        elif checkLine(char,0,3,6):
            return True
        elif checkLine(char,1,4,7):
            return True
        elif checkLine(char,2,5,8):
            return True
        elif checkLine(char,0,4,8):
            return True
        elif checkLine(char,2,4,6):
            return True
        

def checkLine(char,case1,case2,case3):
    print(char,tableau)
    if tableau[case1]== char and tableau[case2]== char and tableau[case3]==char:
        return True
   


while (True):    
    
    if i%2==0:#player1    
        choice=int(input("choose a place to put your X (PLAYER1)"))
        choice=choice-1
        if tableau[choice] != 'X' and tableau[choice] != 'O':
            tableau[choice]='X'
            if checkAll('X') == True:
                show()
                print ("~ ~ ~ ~ ~X Wins~ ~ ~ ~ ~")
                if replay():
                    del tableau[:]
                    continue
                else:
                 print("Thank You for playing Tic Tac Toe BY Noobie Noobie\n bye bye bye")
                 break  
        else:
            print("__________________________\n-------------------------\nTHIS PLACE IS ALREADY TOKEN\n-------------------------\n__________________________")
            show()
            print("__________________________\n-------------------------\nTHIS PLACE IS ALREADY TOKEN\n-------------------------\n__________________________")
        
    else:#player2
        choice=int(input("choose a place to put your O (PLAYER2)"))
        choice=choice-1
        if tableau[choice] != 'X' and tableau[choice] != 'O':
            tableau[choice]='O'
            if checkAll('O') == True:
                print ("~ ~ ~ ~ ~O Wins~ ~ ~ ~ ~")
                break
        else:
            print("__________________________\n-------------------------\nTHIS PLACE IS ALREADY TOKEN\n-------------------------\n__________________________")
            show()
            print("__________________________\n-------------------------\nTHIS PLACE IS ALREADY TOKEN\n-------------------------\n__________________________")
    i+=1
    show()
    

   

    
        
