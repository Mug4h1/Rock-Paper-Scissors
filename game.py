import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import random

choices = ["Rock", "Paper", "Scissors"]

def result(message):
    Label(window, text=message, font=('Times New Roman', 20, 'bold')).place(x=157, y=300)


def game(choice):
    computer = random.choice(choices)
    Label(window, text=computer, foreground="Green", font=('Times New Roman', 10)).place(x=185, y=270)
    if choice == "Rock":
        if computer == "Paper":
            result("You lose!")
        elif computer == "Scissors":
            result("You win!")
        else:
            result("It's a tie!")

    if choice == "Paper":
        if computer == "Scissors":
            result("You lose!")
        elif computer == "Rock":
            result("You win!")
        else:
            result("It's a tie!")
    
    if choice == "Scissors":
        if computer == "Rock":
            result("You lose!")
        elif computer == "Paper":
            result("You win!")
        else:
            result("It's a tie!")



def resize_image(image_path, dimension_x, dimension_y):
    original_image = Image.open(image_path)
    resized_image = original_image.resize((dimension_x, dimension_y))

    return ImageTk.PhotoImage(resized_image)


window = tk.Tk()
window.geometry("425x360")
window.title("Rock, Paper & Scissors")
Label(window, text="ROCK, PAPER & SCISSORS", font=('Times New Roman', 20, 'bold')).place(x=37, y=25)
Label(window, text="What's your pick?", font=('Times New Roman', 10)).place(x=165, y=75)
Label(window, text="Computer chose: ", font=('Times New Roman', 10)).place(x=165, y=250)

rock_image = resize_image("C:/Users/Pratham/Desktop/Mugdha/Python/Rock-Paper-Scissors/rock.png", 100, 100)
paper_image = resize_image("C:/Users/Pratham/Desktop/Mugdha/Python/Rock-Paper-Scissors/paper.png", 100, 100)
scissors_image = resize_image("C:/Users/Pratham/Desktop/Mugdha/Python/Rock-Paper-Scissors/scissors.png", 100, 100)

rock = Button(window, text="Rock", image=rock_image, cursor="hand2", command=lambda: game("Rock"))
paper = Button(window, text="Paper", image=paper_image, cursor="hand2", command=lambda: game("Paper"))
scissors = Button(window, text="Scissors", image=scissors_image, cursor="hand2", command=lambda: game("Scissors"))

rock.place(x=10, y=125)
paper.place(x=160, y=125)
scissors.place(x=310, y=125)

window.mainloop()