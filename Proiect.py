from turtle import *
screen=getscreen()
screen.setup(800,800)

def Lyla():
    for i in range(5):
        dot(120, "red")
        up()
        left(70)
        forward(100)
        down()
    up()
    goto(-50,60)
    dot(130,"pink")
    down()

def game_over():
    screen.bgpic("game_over.png")
    exit()

def you_won():
    screen.bgpic("you_won.png")
    exit()

from turtle import *

screen = Screen()
screen.bgcolor("#fffc86")

def story():
    screen.bgpic("background2.png")
    penup()
    setpos(-370, -270)
    pendown()
    one=write('There was once a flower named Lyla who was very popular among\nthe garden’s residents like Larry the Snail or Sony the Garden Gnome.', font=("Helvetica", 14, "normal"))
    ontimer(clear, t=1000)

def Stats_Draw():
    #Prep for box
    pen(pencolor="black", fillcolor="black", pensize=3)
    penup()
    setpos(175,310)
    pendown()
    begin_fill()
    x=210
    y=80

    #Draw box for stats
    for i in range (0,2):
        forward(x)
        left(90)
        forward(y)
        left(90)
    end_fill()

    #prep for health
    penup()
    pen(pencolor="#C0FF00",fillcolor="#C0FF00",pensize = 2, speed=0)

    #Draw Health stat
    sqr_len=40
    setpos(180,355)
    for i in range (0,5):
        begin_fill()
        for j in range(0,2):
            forward(sqr_len)
            left(90)
            forward(sqr_len)
            left(90)
        end_fill()
        forward(sqr_len+3)
    penup()

    #Prep for Love
    pen(pencolor="#d81583",fillcolor="#d81583",pensize = 1, speed=0)
    setpos(180,310)
    pendown()

    #Draw Love stat
    for i in range (0,5):
        begin_fill()
        for j in range(0,2):
            forward(sqr_len)
            left(90)
            forward(sqr_len)
            left(90)
        end_fill()
        forward(sqr_len+3)
    
Stats_Draw()
Lyla()
story()
mainloop()
