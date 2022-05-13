
import random



def targetscore():
    global tscore
    tscore=random.randint(1,16)
    return tscore
def dicerolling():
    global dice
    dice=random.randint(1,6)
    return dice
def parti1(player1,i):
        print(" ")
        print(" ")
        Player1 = player1
        print(".....",Player1,".....")
        if (i==0):
            global totalpointpl1
            totalpointpl1=0
        status=input("Do you want to roll the dice: (y/n)")
        if status== "y":
            
            print("Rolling first Dice...........")
            firstroll=dicerolling()
            print("Result = ",firstroll)
            print("Rolling second Dice...........")
            secondroll=dicerolling()
            print("Result = ",secondroll)
            total= firstroll+secondroll
            print("Total after rolling two dice is :", total)
            if total == tscore:
                player1point= tscore
                
                totalpointpl1 = (totalpointpl1 + player1point)
                
            else:
                player1point= 0
                totalpointpl1 = (totalpointpl1 + player1point)
            
        else:
             quit()
        print(" ")
        print("                     Your points=",totalpointpl1)
        return None
       
def parti2(player2,i):
        #print("OOOOOO",i)
        print(" ")
        print(" ")
        if (i==0):
            global totalpointpl2
            totalpointpl2=0
        Player2 = player2
        print(".....",Player2,".....")
        status=input("Do you want to roll the dice: (y/n)")
        if status== "y":
            print("Rolling first Dice...........")
            firstroll=dicerolling()
            print("Result = ",firstroll)
            print("Rolling second Dice..........")
            secondroll=dicerolling()
            print("Result = ",secondroll)
            total= firstroll+secondroll
            print("Total after rolling two dice is :", total)
            if total == tscore:
                player2point= tscore
               
                totalpointpl2 = totalpointpl2 + player2point
                
            else:
                player2point= 0
                totalpointpl2= totalpointpl2 + player2point
         
        else:
             quit()
        print(" ")
        print("                     Your points=",totalpointpl2)

    



print("*************Chicago***************")

print(" This is an easy and fun dice game intended for two players")
rule="""
      The Game consists of 11 rounds.
      Each player get two chances to roll the dice and if the total matches the target score.
      BINGO!!! tha player get that point.
      after 11 round the total points are added and who get the greatest is the winner.
     """

print("The Game Begin")
print(" ")
print(" ")
print("PLAYER1")
print(" ")

player1=input("Enter your name:").lower().strip()
print(" ")
print("PLAYER2")
print(" ")
player2=input("Enter your name:").lower().strip()
print(" ")
player=input("who is the player :")

if player == player1:
    pass
elif player == player2:
     pass
else:
    print("Wrong player")
    quit()

turn=11

for i in range(turn):
    #print((11-i)," turn more")
   
    print(" ")
    print(" ")
    print("-----------------------",(i + 1),"Turn ------------------------------")

    print("**targetscore**",targetscore())
    if i == 0 and player == player1:
        parti1(player1,i)
        parti2(player2,i)
        firstplayer= player1
         
    elif i == 0 and player == player2:
       
        parti2(player2,i)
        parti1(player1,i)
        firstplayer=player2
        
    if firstplayer == player1 and i != 0:
        
        parti1(player1,i)
        parti2(player2,i)
        
    if firstplayer == player2 and i != 0:
       
        parti2(player2,i)
        parti1(player1,i)
        
    if i== 10:
         if totalpointpl1 > totalpointpl2:
             print(" ")
             print(" ")
             print("...............The winner is.................")
             print(" ")
             print(player1)
         elif totalpointpl1 < totalpointpl2:
             print(" ")
             print(" ")
             print("................The winner is.................")
             print(" ")
             print(player2)
         elif totalpointpl1 == totalpointpl2:
             print(" ")
             print(" ")
             print("...............Both are winners...............")
             
         
        

