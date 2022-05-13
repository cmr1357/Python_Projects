
#############################Project-Mad Lib Generator############################




    
def madlib():
        GirlsName=input("A girl's name :")
        Number=input("A number :")
        Emotion=input("An emotion :")
        Place=input("A place :")
        BoysName=input("A boy's Name :")
        AnotherNumber=input("Another Number :")
        NumLessFifty=input("A Number Less than 50 :")
        MoreNumber=input("One more number :")
        ReindeerName=input("A Reindeer's Name :")
        AnotherEmotion=input("Another Emotion :")


        Action=input("What you want to do build story or start over?build/start")

        if Action == "build":
            
            print("     ")
            print(f"{'STORY THE CHRISTMAS SURPRISE':^100}")
            print("     ")
        

            Story=   """
                     {0} woke up one Christmas Day to find that she had no presents!
                     On the end of her bed she found a letter from {1} of Santa's eleves.
                     It said that Santa was very {2}.
                     After she had read the letter, She found herself being whisked off to the {3}.
                     There she met an elf whose name was {4}. He said that he was Santa's helper.
                     Because Santa was happy,
                     {0} had to deliver all {5} presents to everyone around the world before they woke up.
                     {8} was in front and off they went.
                     It was a hard job but in the end they did it in {6} minutes.
                     When she arrived back home, she found {7} on her bed. She was so {9}.
                     """

            newstring=Story.format(GirlsName,Number,Emotion,Place,BoysName,AnotherNumber,NumLessFifty,MoreNumber,ReindeerName,AnotherEmotion)
            print(newstring)


        else:
            madlib()

 
play=input("Do you want to play Mad lib?y/n")

if play == "y":
    madlib()
else:
    quit()
