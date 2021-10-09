from turtle import *
screen=getscreen()
screen.setup(800,800)
speed(0)
sqr_len=40
health_x = 170
screen = Screen()
screen.bgcolor("#fffc86")
screen.bgpic("background.png")
hideturtle()
dialogue=['Hi, human, I am Lyla! I am extremely sad \nbecause i’ve been separated from my friends.\nI need someone to take care of me.','Will you do that for me?\nYes\nNo\n','Since I was picked up, I’ve been crying \nall night.\n','Do you also cry at night, \nwhen you are alone?\nYes\nNo','I wished I could accomplish my dreams \nwhile I was in the garden. I wanted to \nbecome a model, but my dreams were ruined.','I think you have dreams for the future \nas well, am I right?\nYes\nNo']
storyline=['There was once a flower named Lyla who was\nvery popular among the garden’s residents \nlike Larry the Snail or Sony the Garden Gnome.', 'During the day, she’s very happy and cheerful,\nfeeding off sunlight and social interactions\nwith her peers.','But one tragic day, Grandma picked all the\nmost beautiful flowers in the garden, including\nLyla, to give each of her grandchildren one.', 'Fortunately for you, Grandma has picked\nLyla to be your companion, but now,\nher life depends on you.', 'Check the bar in the top right corner.\nThat is the health bar.\n', 'When you pick the wrong option, \nyou lose a heart.\n', 'When you have no more hearts,\nshe will wither and die.\n', 'Good luck!\n \n']
def SadLayla():
    pen(pencolor="black")
    speed(0)
    up()
    seth(0)
    goto(50,-70)
    down()

    #Petals
    for i in range(5):
        dot(120,"#b74e58")
        up()
        left(70)
        forward(100)
        down()
    
    #Center
    up()
    goto(0,0)
    down()
    dot(130,"#bf9393")

    #Eyes
    for i in range(0,41,40):
        up()
        goto((-20)+i,10)
        down()
        dot(20,"white")
        up()
        goto((-20)+i,10)
        down()
        dot(8)


  
    #Smile
    up()
    goto((-22),-40)
    down()
    pen(pencolor="#d9534f", fillcolor="#ff6f69", pensize=3)
    begin_fill()
    seth(90)
    circle(-25,170)
    right(110)
    circle(110,25)
    end_fill()
    hideturtle()
    
    
def Lyla():

    pen(pencolor="black")
    
    speed(0)
    up()
    goto(50,-70)
    down()

    #Petals
    for i in range(5):
        dot(120,"#d9534f")
        up()
        left(70)
        forward(100)
        down()
    
    #Center
    up()
    goto(0,0)
    down()
    dot(130,"#ffbdbd")

    #Eyes
    for i in range(0,41,40):
        up()
        goto((-20)+i,10)
        down()
        dot(20,"white")
        up()
        goto((-20)+i,10)
        down()
        dot(8)


  
    #Smile
    up()
    goto((-21),-20)
    down()
    pen(pencolor="#d9534f", fillcolor="#ff6f69", pensize=3)
    begin_fill()
    circle(110,25)
    right(110)
    circle(-25,170)
    end_fill()
    hideturtle()

def Drain_Health():
    penup()
    pen(pencolor="black", fillcolor="black",pensize=2, speed=0)
    setpos(health_x,355)
    pendown()
    begin_fill()
    for i in range(0,2):
        forward(sqr_len)
        left(90)
        forward(sqr_len)
        left(90)
    end_fill()

def game_over():
    screen.bgpic("game_over.png")
    exit()

def you_won():
    screen.bgpic("you_won.png")
    exit()

def story():
    screen.bgpic("background2.png")
    for i in range (8):
        up()
        setpos(-370, -330)
        down()
        if i>=4:
            pencolor("#188312")
    
        one= write (storyline[i],align='left', font=("Helvetica", 20, 'normal'))
        ontimer(undo(), t=2000)

def dialog():
    screen.bgpic("background2.png")
    for i in range(6):
        up()
        setpos(-370, -330)
        down()
        if i%2==1:
            up()
            setpos(-370, -350)
            down()
        one= write (dialogue[i],align='left', font=("Helvetica", 20, 'normal'))
        
        ontimer(undo(), t=2000)



def Stats_Draw():
    #Prep for box
    pen(pencolor="black", fillcolor="black", pensize=3)
    penup()
    setpos(165,350)
    pendown()
    begin_fill()
    x=220
    y=85

    #Draw box for stats
    for i in range (0,2):
        forward(x)
        left(90)
        forward(y)
        left(90)
    end_fill()

    #prep for health
    penup()
    pen(pencolor="#C0FF00",fillcolor="#C0FF00",pensize = 2)

    #Draw Health stat
    sqr_len=40
    setpos(170,355)
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
    
Stats_Draw()
Lyla()
story()
ontimer(screen.bgpic("background.png"), t=2000)
dialog()
screen.delay(0)
SadLayla()
screen.delay(1)
mainloop()

