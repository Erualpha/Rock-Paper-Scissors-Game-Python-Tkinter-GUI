from tkinter import *
from PIL import Image, ImageTk
import random

root = Tk()
root.title("RPS")
root.geometry("400x600")
root.resizable(0,0)
root.iconbitmap("icon.ico")

#======Functions=====
scr_player = 0
scr_comp = 0

def score(result):
    global scr_player
    global scr_comp
    if result == "You win!":
        canvas_scoreboard1.delete('all')
        scr_player += 1
        canvas_scoreboard1.create_text(25,20, text=scr_player, fill='white', font=('Bebas', 30))
    if result == "You lose!":
        canvas_scoreboard2.delete('all')
        scr_comp += 1
        canvas_scoreboard2.create_text(25,20, text=scr_comp, fill='black', font=('Bebas', 30))

def rock(a):
    comp = random.choice(["rock", "paper", "scissor"])
    show_picked(a, comp)
    images_picked(a, comp)
    if comp == a:
        show_result("It's a tie!")
    elif comp == "paper":
        show_result("You lose!")
    elif comp == "scissor":
        show_result("You win!")

def paper(b):
    comp = random.choice(["rock", "paper", "scissor"])
    show_picked(b, comp)
    images_picked(b, comp)
    if comp == b:
        show_result("It's a tie!")
    elif comp == "scissor":
        show_result("You lose!")
    elif comp == "rock":
        show_result("You win!")

def scissor(c):
    comp = random.choice(["rock", "paper", "scissor"])
    show_picked(c, comp)
    images_picked(c, comp)
    if comp == c:
        show_result("It's a tie!")
    elif comp == "rock":
        show_result("You lose!")
    elif comp == "paper":
        show_result("You win!")

def show_picked(player, comp):
    canvas_screen1.delete('all')
    canvas_screen2.delete('all')
    player = canvas_screen1.create_text(90,200, text=player.upper(), fill="#302e2f", font=('Bebas', 25))
    comp = canvas_screen2.create_text(90,200, text=comp.upper(), fill="#302e2f", font=('Bebas', 25))

def show_result(e):
    canvas_screen3.delete('all')
    canvas_screen3.create_text(65,10, text=e, fill='white', font=('Bebas', 20))
    score(e)


def images_picked(player, comp):
    if player == "rock":
        canvas_screen1.create_image(10,30, anchor=NW, image=player_rock)
    elif player == "paper":
        canvas_screen1.create_image(5,30, anchor=NW, image=player_paper)
    elif player == "scissor":
        canvas_screen1.create_image(1,30, anchor=NW, image=player_scissor)
    if comp == "rock":
        canvas_screen2.create_image(10,30, anchor=NW, image=comp_rock)
    elif comp == "paper":
        canvas_screen2.create_image(5,30, anchor=NW, image=comp_paper)
    elif comp == "scissor":
        canvas_screen2.create_image(1,30, anchor=NW, image=comp_scissor)

def reset_game():
    canvas_scoreboard1.delete('all')
    canvas_scoreboard2.delete('all')
    canvas_screen1.delete('all')
    canvas_screen2.delete('all')
    canvas_screen3.delete('all')
    global scr_player
    global scr_comp
    scr_player = 0
    scr_comp = 0
    canvas_scoreboard1.create_text(25,20, text=scr_player, fill='white', font=('Bebas', 30))
    canvas_scoreboard2.create_text(25,20, text=scr_comp, fill='black', font=('Bebas', 30))


#======Images=========

player_rock = ImageTk.PhotoImage(Image.open('rock1.png'))
player_paper = ImageTk.PhotoImage(Image.open('paper1.png'))
player_scissor = ImageTk.PhotoImage(Image.open('scissor1.png'))
comp_rock = ImageTk.PhotoImage(Image.open('rock.png'))
comp_paper = ImageTk.PhotoImage(Image.open('paper.png'))
comp_scissor = ImageTk.PhotoImage(Image.open('scissor.png'))

logo = ImageTk.PhotoImage(Image.open('logo.png'))
scoreboard = ImageTk.PhotoImage(Image.open('scoreboard.png'))
scoreboard1 = ImageTk.PhotoImage(Image.open('scoreboard1.png'))
bg = ImageTk.PhotoImage(Image.open('bg.png'))
rock_button = ImageTk.PhotoImage(Image.open('rock_button.png'))
paper_button = ImageTk.PhotoImage(Image.open('paper_button.png'))
scissor_button = ImageTk.PhotoImage(Image.open('scissor_button.png'))
new_game = ImageTk.PhotoImage(Image.open('new_game.png'))
quit_game = ImageTk.PhotoImage(Image.open('quit_game.png'))

#=======CanvasWidgets====
canvas_main = Canvas(root, width = 400, height = 600)
canvas_main.place(x=-2, y=0)
canvas_main.create_image(0,0, anchor = NW, image = bg)
canvas_main.create_image(90,115, anchor = NW, image = scoreboard1)
canvas_main.create_image(12,70, anchor = NW, image = scoreboard)
canvas_main.create_image(65,0, anchor = NW, image = logo)
canvas_main.create_text(110,98, text='PLAYER', fill='black', font=('Bebas',13))
canvas_main.create_text(295,98, text='COMPUTER', fill='black', font=('Bebas',13))

canvas_screen1 = Canvas(root, bg='#709dff', width=180, height=220, highlightbackground='#143d59')
canvas_screen1.place(x=10, y=167)
canvas_screen2 = Canvas(root, bg='#ff2e2a', width=180, height=220, highlightbackground='#143d59')
canvas_screen2.place(x=205, y=167)
canvas_screen3 = Canvas(root, bg='#2d292a', width=130, height=25, highlightthickness=0)
canvas_screen3.place(x=140, y=130)

canvas_scoreboard1 = Canvas(root, bg='black', width=50, height=40, highlightbackground='#D3D3D3')
canvas_scoreboard1.place(x=147, y=78)
canvas_scoreboard2 = Canvas(root, bg='white', width=50, height=40, highlightbackground='#D3D3D3')
canvas_scoreboard2.place(x=199, y=78)
canvas_scoreboard1.create_text(30,20, text=scr_player, fill='white', font=('Bebas',30))
canvas_scoreboard2.create_text(30,20, text=scr_player, fill='black', font=('Bebas',30))

#======Button======
button1 = Button(canvas_main, bg='#e8bf23', border=1, image=rock_button, command=lambda: rock("rock")).place(x=5, y=400)
button2 = Button(canvas_main, bg='#2ed755', border=1, image=paper_button, command=lambda: paper("paper")).place(x=205, y=400)
button3 = Button(canvas_main, bg='#03a8fd', border=1, image=scissor_button, command=lambda: scissor("scissor")).place(x=100, y=465)

button4 = Button(canvas_main, bg='#03a8fd', border=1, image=new_game, command=reset_game).place(x=40, y=550)
button5 = Button(canvas_main, bg='#ff6546', border=1, image=quit_game, command=root.quit).place(x=220, y=550)




root.mainloop()