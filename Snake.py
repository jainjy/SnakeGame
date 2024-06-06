from tkinter import *
from customtkinter import *
import random
import time
import sys
import sqlite3
class Tile:
    def __init__(self,x,y):
        self.x=x
        self.y=y


j=1
num=20
connection=sqlite3
ROWS,COLS,TILE=num,num,15
WIN_W=num*ROWS
WIN_H=num*COLS
game_over=False
score=0
jouer=False
vitesses=[290,190,100]
speed=vitesses[1]
texte="normale"
best_score=[50,40,30]

window=CTk()
window.title("snake")

window.resizable(False,False)
window.geometry(f"{WIN_W}x{WIN_H}+{400}+{0}")
window_width=window.winfo_width()
window_height=window.winfo_height()
# photo=PhotoImage(file="serpant.jpg")
def start():
    global canvasP
    canvasP.destroy()
    canvasP=CTkCanvas(window,bg="grey",width=WIN_W,height=WIN_H,borderwidth=0,highlightthickness=0)
    canvasP.pack()
    # img=PhotoImage(file="serpant.png")
    titre=CTkLabel(canvasP,text="SNAKE GAME",bg_color="brown",font=("Times",20,"bold")).place(x=130,y=50)
    # canvasP.create_image(30,30,image=img)
    CTkButton(canvasP,text="jouer",hover_color="lime green",command=play).place(x=130,y=200)
    CTkButton(canvasP,text="Mode",hover_color="lime green",command=Niveau).place(x=130,y=250)
    CTkButton(canvasP,text="best score",hover_color="lime green",command=best).place(x=130,y=300)
    quiter=CTkButton(canvasP,text="Quiter",hover_color="red",bg_color="red",corner_radius=20,command=window.destroy)
    quiter.place(x=130,y=350)


def Niveau():
    global canvasP,speed,vitesses,texte,j
    def vitesse(sped):
        global speed
        speed=sped
        Niveau()

    if speed==vitesses[0]:
        texte="facile"
        j=0
    elif(speed==vitesses[1]):
        texte="normale"
        j=1
    elif(speed==vitesses[2]):
        texte="difficile"
        j=2
    
    canvasP.destroy()
    canvasP=CTkCanvas(window,bg="grey",width=WIN_W,height=WIN_H,borderwidth=0,highlightthickness=0)
    canvasP.pack()
    canvasP.create_text(WIN_W/2,WIN_H/8,text=f"Mode {texte}")
    CTkButton(canvasP,text="facile",hover_color="yellow",command=lambda:vitesse(vitesses[0])).place(x=130,y=100)
    CTkButton(canvasP,text="normal",hover_color="green",command=lambda:vitesse(vitesses[1])).place(x=130,y=150)
    CTkButton(canvasP,text="difficile",hover_color="red",command=lambda:vitesse(vitesses[2])).place(x=130,y=200)
    CTkButton(canvasP,text="retourner",hover_color="red",bg_color="red",corner_radius=20,command=start).place(x=130,y=350)

def play():
    global jouer,canvasP
    jouer=True
    canvasP.destroy()
    jouers()
    return

def best():
    global canvasP
    canvasP.destroy()
    canvasP=CTkCanvas(window,bg="grey",width=WIN_W,height=WIN_H,borderwidth=0,highlightthickness=0)
    canvasP.pack()
    CTkLabel(canvasP,text=f"facile :{best_score[0]}",text_color="yellow",font=("Times",18,"bold")).place(x=110,y=100)
    CTkLabel(canvasP,text=f"Normale :{best_score[1]}",text_color="green",font=("Times",18,"bold")).place(x=110,y=150)
    CTkLabel(canvasP,text=f"Difficile :{best_score[2]}",text_color="red",font=("Times",18,"bold")).place(x=110,y=200)
    CTkButton(canvasP,text="retourner",hover_color="red",bg_color="red",corner_radius=20,command=start).place(x=130,y=350)
    return


canvasP=CTkCanvas(window,bg="grey",width=WIN_W,height=WIN_H,borderwidth=0,highlightthickness=0)
canvasP.pack()

snake=Tile(0,0)
snake_body=[Tile(TILE*-3,0),Tile(TILE*-2,0),Tile(TILE*-1,0)]
food=Tile(random.randint(0,COLS-1)*TILE,random.randint(0,ROWS-1)*TILE)
velocityY=0
velocityX=1
start()
def jouers():

    canvas=CTkCanvas(window,bg="black",width=WIN_W,height=WIN_H,borderwidth=0,highlightthickness=0)
    canvas.pack()
    window.update()
    window.geometry(f"{WIN_W}x{WIN_H}+{400}+{0}")
    window_width=window.winfo_width()
    window_height=window.winfo_height()     
    def change_direction(e):
        global velocityX,velocityY,snake_body
        
        if(e.keysym=="Up" and velocityY!=1 ):
            velocityX=0
            velocityY=-1
        elif(e.keysym=="Down" and velocityY!=-1):
            velocityX=0
            velocityY=1
        elif(e.keysym=="Left" and velocityX!=1):
            velocityX=-1
            velocityY=0
        elif(e.keysym=="Right" and velocityX!=-1):
            velocityX=1
            velocityY=0
        elif(e.keysym=="space"):
            velocityX=0
            velocityY=0

    def move():
        global snake,food,tile,game_over,snake_body,score
        if(not canvas):
            jouers()
        if(game_over):
            return
        
        if(snake.x<0 or snake.x>=window_width or snake.y<0 or snake.y>=window_height):
            game_over=True
            return

        for tile in snake_body:
            if(snake.x==tile.x and snake.y==tile.y):
                game_over=True
                return 
            elif(food.x==tile.x and food.y==tile.y):
                score+=1
        if(snake.x==food.x and snake.y==food.y):
            snake_body.append(Tile(food.x,food.y))
            food.x=random.randint(0,COLS-1)*TILE
            food.y=random.randint(0,ROWS-1)*TILE
            score+=1

        for i in range(len(snake_body)-1,-1,-1):
            tile=snake_body[i]
            if(i==0):
                tile.x=snake.x
                tile.y=snake.y
            else:
                prev_tile=snake_body[i-1]
                tile.x=prev_tile.x
                tile.y=prev_tile.y

        snake.x+=velocityX*TILE
        snake.y+=velocityY*TILE
        time.sleep(0.0001)
    
    def draw():
        global snake,food,snake_body,score,speed,best_score,j
        if(jouer):
            move()
            try:
                canvas.delete("all")
                canvas.create_rectangle(snake.x,snake.y,snake.x+TILE,snake.y+TILE,fill="lime green")
                canvas.create_rectangle(food.x,food.y,food.x+TILE,food.y+TILE,fill="red",outline="yellow")
            except:
                pass
            for tile in snake_body:
                canvas.create_rectangle(tile.x,tile.y,tile.x+TILE,tile.y+TILE,fill="green")

            if(game_over):
                if(score>best_score[j]):
                    best_score[j]=score
                canvas2=CTkCanvas(canvas,bg="black",width=WIN_W,height=WIN_H,borderwidth=0,highlightthickness=0)
                canvas2.place(x=0,y=0)
                canvas2.create_text(window_width/2,window_height/4,text=f"GAME OVER ",font=("",25,"bold"),fill="red")
                canvas2.create_text(window_width/2,window_height/4+30,text=f"SCORE :{score}",font=("",25,"italic"),fill="red")
                ressayer=CTkButton(canvas2,text="Ressayer",hover_color="lime green",command=lambda:again())
                ressayer.place(x=130,y=250)
                quiter=CTkButton(canvas2,text="Quiter",command=lambda:exit())
                quiter.place(x=130,y=300)
                def again():
                    global score,snake,food,snake_body,score,velocityX,velocityY,game_over
                    game_over=False
                    score=0
                    snake=Tile(0,0)
                    snake_body=[Tile(TILE*-3,0),Tile(TILE*-2,0),Tile(TILE*-1,0)]
                    food=Tile(random.randint(0,COLS-1)*TILE,random.randint(0,ROWS-1)*TILE)
                    velocityY=0
                    velocityX=1
                    canvas.destroy()
                    canvas2.destroy()
                    jouers()
                def exit():
                    global jouer,game_over,velocityX,velocityY,snake_body,snake,food,tile,game_over,score
                    jouer=False
                    game_over=False
                    score=0
                    snake=Tile(TILE*3,0)
                    snake_body=[Tile(0,0),Tile(TILE,0),Tile(TILE*2,0)]
                    food=Tile(random.randint(0,COLS-1)*TILE,random.randint(0,ROWS-1)*TILE)
                    velocityY=0
                    velocityX=1
                    canvas.destroy()
                    canvas2.destroy()
                    start()

            else:
                canvas.create_text(30,window_height-TILE,text=f"SCORE:{score}",fill="white",font=("",10,"bold"))
        window.after(speed,draw)
        
    draw()

    window.bind("<KeyRelease>",change_direction)
window.mainloop()
