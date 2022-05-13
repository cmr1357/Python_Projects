import random


def Magic():
    MagicNumber = random.randint(1,100)

    

    turn =5

    for i in range(turn):
    
        userinput=int(input("Enter a number between 1 and 100 : "))
        if userinput>100:
            print("Your guess is too high, pick a number between 1 and 100")
            Magic()
        if userinput<1:
            print("Your guess is too low, pick a number between 1 and 100")
            Magic()
            
        if userinput<MagicNumber:
            print ("Low Guesses")
            print((4-i), "More turns")
        elif userinput > MagicNumber:
            print("High Guesses")
            print((4-i), "More turns")
        else:
            print("It took you",( i+1),"turns to guess my number which was",MagicNumber)
            PlayAgain=input("Play the game again y/n: ")
            if PlayAgain == "y":
                Magic()
            else:
                quit()
print(" ")
print(" ")
print("Guess the secret number in the magician's hat. If your guess is too high or too low, you'll get a hint.")
print(" ")
print(" ")
print("You have total 5 chances to guess")
print(" ")
print(" ")
print("Let us Begin...........")
print(" ")
print(" ")
Magic()
