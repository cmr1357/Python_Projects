
from wordslist import word_list
import random
from Hangman import stage
print("The Game begins....")
print("\n")

def getword():
    pick=random.choice(word_list)
    #print(pick)
    return pick.upper()


def game(pick):
    letters="-"*len(pick)
    print("\n")
    print(letters)
    completed=False
    count=6
    wrongGuess=0
    guessed_letters=[]
    completion=0
    
    while count!= 0 and completed== False:
        guess= input("Enter your letter : ").upper()
        
           # print(stage[wrongGuess])
       # print("count=",count)
        if guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter")
                print("\n")
                #print(stage[wrongGuess])
            elif guess in pick:
                print("good job",guess, "is in the word")
                print("\n")
                guessed_letters.append(guess)
                #print("guessed_letters",guessed_letters)
                word_as_list=list(letters)
                #print(word_as_list)
                indices=[i for i, letter in enumerate(pick) if letter == guess]
                #print(indices)
               
                for index in indices:
                    completion += 1
                    #print(completion,len(pick))
                    #print(index,"index")
                    word_as_list[index]=guess
                    
                letters="".join(word_as_list)
                print(letters)
                print(stage[wrongGuess])
                if completion == len(pick):
                    completed=True

            else:

                print("Wrong guess try again")
                print("\n")
                count = count- 1
                wrongGuess +=1
                print(stage[wrongGuess])
                print(letters)
                guessed_letters.append(guess)
                
        else:
            print("Oh... you entered a number it should be a letter")
        if completed == True:
            print("\n")
            print("Great the word is",pick)
            print("\n")
                
    if count == 0:
        print("Man died...")
        print("The word is",pick)
        print("\n")



def main():
    pick=getword()
    game(pick)
    print("\n")
    playagain=input("Do you want to try another one? Y/N: ").upper()
    if playagain == "Y":
        main()
                
    
if __name__ == "__main__":
    main()


