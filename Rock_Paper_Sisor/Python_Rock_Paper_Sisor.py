from tkinter import *
from PIL import Image,ImageTk
from random import randint

#main window
root = Tk()
root.title("Rock,Paper,Scissors")
root.configure(bg="#9b59b6")

#picture
rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissor-user.png"))

rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissor.png"))
#insert picture

user_label = Label(root,image=rock_img,bg="#9b59b6")
comp_label = Label(root, image= rock_img_comp,bg="#9b59b6")

comp_label.grid(row=1,column=0)
user_label.grid(row=1, column=4)

#scores

playerscore = Label(root,text=0, font=100,bg="#9b59b6",fg="white")
computerscore= Label(root, text=0,font=100,bg="#9b59b6",fg="white")
computerscore.grid(row=1, column=1)
playerscore.grid(row=1, column=3)
#indicators
user_indicator=Label(root, font=50,text="USER",bg="#9b59b6",fg="white")
comp_indicator=Label(root, font=50,text="COMPUTER",bg="#9b59b6",fg="white")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

#messages

msg=Label(root, font=50,bg="#9b59b6",fg="white")
msg.grid(row=3, column=2)

#update message

def updateMessage(x):
    msg['text'] = x

#update user score

def updateUserScore():
    score= int(playerscore["text"])
    score += 1
    playerscore["text"] = str(score)

#update computer score
def updateCompScore():
    score= int(computerscore["text"])
    score += 1
    computerscore["text"] = str(score)

#check winner

def checkwin(player, computer):
    if player == computer:
        updateMessage("Its a tie!!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player =="paper":
        if computer =="scissor":
            updateMessage("You loose")
            updateCompScore()
        
        else:
            updateMessage("You Win")
            updateUserScore()

    elif player =="scissor":
        if computer =="rock":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()  
    else:
        pass


#update choices
choices=["rock","paper","scissor"]

def updatechoice(x):

#for computer
    computerchoice = choices[randint(0,2)]
    if computerchoice=="rock":
        comp_label.configure(image=rock_img_comp)
    elif computerchoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)
#for user
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)
    checkwin(x,computerchoice)
#buttons

rock=Button(root,width=20, height=2, text="ROCK", bg="#FF3E4D", fg="white",command = lambda:updatechoice("rock")).grid(row=2, column=1)
paper=Button(root,width=20, height=2, text="PAPER", bg="#FF3E4D", fg="white",command = lambda:updatechoice("paper")).grid(row=2, column=2)
sissor=Button(root,width=20, height=2, text="SCISSOR", bg="#FF3E4D", fg="white",command = lambda:updatechoice("scissor")).grid(row=2, column=3)


root.mainloop()
