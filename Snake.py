from customtkinter import *
import random
from tkinter import PhotoImage
import time
pause=False
taille=10
Open=open("score.txt","r")
best_score=Open.readlines()
i=int(best_score[3])
Open.close()
class Snake:
    def __init__(self):
        self.touch=False
        self.x=30
        self.y=30
        self.body=[[20,30],[10,30],[0,30]]
        self.score=0
        self.not_game_over=True
        self.directionY=0
        self.directionX=1  
        self.vitesse=[300,200,100]
        self.niveau=["Facile","Normal","Difficile"]
class menu:
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.fenetre=CTk()
        self.fenetre.title("Snake Game")
        self.logo=PhotoImage(file="im.png")
        self.icon=PhotoImage(file="icon.png")
        self.fenetre.iconphoto(True,self.icon)
        self.fenetre.geometry(f"{self.width}x{self.height}+{self.width+100}+{self.height/4}")
        self.fenetre.resizable(False,False)
    def canvasP(self,back):
        self.canvas=CTkCanvas(self.fenetre,background=back,width=self.width,height=self.height,highlightthickness=0)
        self.canvas.pack()   
    def start(self): 
        self.canvasP("#007de6")
        self.canvas.create_image(self.width/2,self.height/5, image=self.logo)
        self.button=CTkButton(self.canvas,text="Jouer",command=init,width=200,fg_color="#296")
        self.button.place(x=self.width/4,y=self.height/2)
        self.button=CTkButton(self.canvas,text="Niveau",command=self.level,width=200,fg_color="#296")
        self.button.place(x=self.width/4,y=self.height/2+50)
        self.button=CTkButton(self.canvas,text="Best score",command=self.best,width=200,fg_color="#296")
        self.button.place(x=self.width/4,y=self.height/2+100)
        self.button=CTkButton(self.canvas,text="Quitter",fg_color="red",command=self.fenetre.destroy)
        self.button.place(x=self.width/3,y=self.height/2+150)
    def over(self):#affichage du game over
        global snake
        if(int(best_score[i])==snake.score):
            self.canvas.create_text(self.width/2,self.height/5,fill="#942",text=f"felicitation new best",font=("Trattatello",30,"italic"))
        else:
            self.canvas.create_text(self.width/6,self.height//15,fill="white",text=f"Best score:{best_score[i]}",font=("Trattatello",15,"bold"))
        self.canvas.create_text(self.width/1.2,self.height//14,fill="#362",text=f"{snake.niveau[i].upper()}",font=("arial",15,"italic"))
        self.canvas.create_text(self.width/2,self.height/3,fill="red",text="Game Over",font=("arial",40,"bold"))
        self.canvas.create_text(self.width/2,self.height//2,fill="#282",text=f"Score:{snake.score}",font=("arial",20,"italic"))
        self.button=CTkButton(self.canvas,text="Reesseyer",command=rejouer,width=200,fg_color="#669") 
        self.button.place(x=self.width/4,y=self.height/2+50)
        self.button=CTkButton(self.canvas,text="Quitter",command=self.fenetre.destroy,fg_color="red")
        self.button.place(x=50,y=self.height/2+150)
        self.button=CTkButton(self.canvas,text="Menu",command=menus)
        self.button.place(x=200,y=self.height/2+150)
    def best(self):
        global best_score,Open
        Open=open("score.txt","r")
        best_score=Open.readlines()
        self.canvas.destroy()
        self.canvasP("#499")
        self.button=CTkLabel(self.canvas,text=f"Facile    =>{best_score[0]}",font=("arial",20,"bold"),text_color="yellow",width=150)
        self.button.place(x=self.width/8,y=self.height/10)
        self.button=CTkLabel(self.canvas,text=f"Moyen   =>{best_score[1]}",font=("arial",20,"bold"),text_color="green",width=150)
        self.button.place(x=self.width/8,y=self.height/10+50)
        self.button=CTkLabel(self.canvas,text=f"Difficile =>{best_score[2]}",font=("arial",20,"bold"),text_color="red",width=150)
        self.button.place(x=self.width/8,y=self.height/10+100)
        self.button=CTkButton(self.canvas,text="reset",width=50,command=lambda:reset_score(0),fg_color="#631")
        self.button.place(x=self.width-100,y=self.height/10)
        self.button=CTkButton(self.canvas,text="reset",width=50,command=lambda:reset_score(1),fg_color="#631")
        self.button.place(x=self.width-100,y=self.height/10+50)
        self.button=CTkButton(self.canvas,text="reset",width=50,command=lambda:reset_score(2),fg_color="#631")
        self.button.place(x=self.width-100,y=self.height/10+100)
        self.button=CTkButton(self.canvas,text="Reset All",command=reset_score_all,fg_color="#601")
        self.button.place(x=self.width/3,y=self.height/2+100)
        self.button=CTkButton(self.canvas,text="Quitter",command=self.fenetre.destroy,fg_color="red")
        self.button.place(x=50,y=self.height/2+150)
        self.button=CTkButton(self.canvas,text="Back",command=menus)
        self.button.place(x=200,y=self.height/2+150)
        Open.close()
    def level(self):
        global snake
        self.canvas.destroy()
        self.canvasP("#499")
        
        self.texte=CTkLabel(self.canvas,text=f"Niveau Actuel:{snake.niveau[i]}",width=200,height=35,font=("Courier New",20,"bold"))
        self.texte.place(x=self.width/4.5,y=self.height/10) 
        self.button=CTkButton(self.canvas,text="Facile",command=lambda:change_level(0),width=200,height=35,fg_color="#394")
        self.button.place(x=self.width/4,y=self.height/2.5)
        self.button=CTkButton(self.canvas,text="Moyen",command=lambda:change_level(1),width=200,height=35,fg_color="#451")
        self.button.place(x=self.width/4,y=self.height/2.5+50)
        self.button=CTkButton(self.canvas,text="Difficile",command=lambda:change_level(2),width=200,height=35,fg_color="#600")
        self.button.place(x=self.width/4,y=self.height/2.5+100)
        self.button=CTkButton(self.canvas,text="Quitter",command=self.fenetre.destroy,fg_color="red")
        self.button.place(x=50,y=self.height/2+150)
        self.button=CTkButton(self.canvas,text="Back",command=menus)
        self.button.place(x=200,y=self.height/2+150)

def change_level(nombre):
    global jeu,i
    Open=open("score.txt","w")
    Open.write(f"{int(best_score[0])}\n{int(best_score[1])}\n{int(best_score[2])}\n{int(nombre)}")
    Open.close()
    i=nombre
    jeu.texte.configure(text=f"Niveau Actuel:{snake.niveau[nombre]}")

def change_best():
    global snake,i,Open,best_score
    if(snake.score>int(best_score[i])):
        best_score[i]=snake.score
        Open=open("score.txt","w")
        Open.write(f"{int(best_score[0])}\n{int(best_score[1])}\n{int(best_score[2])}\n{int(best_score[3])}")
        Open.close()

def reset_score_all():
    global Open,jeu,best_score
    Open=open("score.txt","w")
    Open.write(f"0\n0\n0\n{best_score[3]}")
    Open.close()
    jeu.best()

def reset_score(nombre):
    global Open,jeu
    best_score[nombre]=0
    Open=open("score.txt","w")
    Open.write(f"{int(best_score[0])}\n{int(best_score[1])}\n{int(best_score[2])}\n{int(i)}")
    Open.close()
    jeu.best()       

def reset():
    global jeu,snake
    jeu.canvas.delete("all")
    snake.not_game_over=True
    snake.score=0
    snake.directionX=1
    snake.directionY=0
    snake.body=[[20,30],[10,30],[0,30]]
    snake.x=30
    snake.y=30

def menus():
    global jeu
    reset()
    jeu.fenetre.after_cancel(id)
    jeu.canvas.destroy()
    jeu.start()

def rejouer():
    global snake,jeu,id
    reset()
    jeu.canvas.destroy()
    jeu.fenetre.after_cancel(id)
    jeu.start()
    init()   

def init():
    global jeu,snake
    snake.touch=True
    jeu.canvas.destroy()
    jeu.canvasP("#000")
    pomme()
    play()

def pomme():
    global xPomme,yPomme,id,taille
    xPomme=(random.randint(0,int((jeu.width)/taille)-1))*taille
    yPomme=(random.randint(0,int((jeu.height)/taille)-3))*taille

def play():
    global jeu,snake,id,score_affichage,score_best,help
    collision()
    if(snake.not_game_over):
        if(snake.x==30 and snake.y==30 and snake.score==0) :
            score_affichage=CTkLabel(jeu.canvas,text=f"score:{snake.score}")
            score_affichage.place(x=5,y=jeu.height-25)
            score_best=CTkLabel(jeu.canvas,text=f"best-score:{best_score[i]}")
            score_best.place(x=jeu.width-90,y=jeu.height-20)
            help=CTkLabel(jeu.canvas,text=f"Press Space to Pause",font=("",10,"bold"),text_color="#234")
            help.place(x=jeu.width/3,y=jeu.height-25)
        manger()   
        dessiner()
    id=jeu.fenetre.after(snake.vitesse[i],play)

def collision():
    global snake,jeu,id
    if(snake.x<0 or snake.x>=jeu.width or snake.y<0 or snake.y>=jeu.height ):
        jeu.canvas.destroy()
        snake.not_game_over=False
        jeu.canvasP("#012")
        snake.touch=False
        jeu.over()  
    for tile in snake.body:
        if(tile[0]==snake.x and tile[1]==snake.y):
            jeu.canvas.destroy()
            snake.not_game_over=False
            jeu.canvasP("#012")
            jeu.over() 

def manger():
    global jeu,snake,xPomme,yPomme,score_affichage
    if(xPomme==snake.x and yPomme==snake.y):
        snake.body.append([xPomme,yPomme])
        snake.score+=1
        score_affichage.configure(text=f"score:{snake.score}")
        change_best()
        pomme()

def changer(e):
    global snake,pause,jeu,lastY,lastX,id,i
    if(snake.touch):
        if(e.keysym=="Up" and snake.directionY!=1):
            snake.directionX=0
            snake.directionY=-1
        elif(e.keysym=="Down" and snake.directionY!=-1):
            snake.directionX=0
            snake.directionY=1
        elif(e.keysym=="Left" and snake.directionX!=1):
            snake.directionX=-1
            snake.directionY=0
        elif(e.keysym=="Right" and snake.directionX!=-1):
            snake.directionX=1
            snake.directionY=0 
        elif(e.keysym=="space"):
            if(pause):
                j=3
                pause=False
                snake.directionX=lastX
                snake.directionY=lastY
                id=jeu.fenetre.after(snake.vitesse[i],play)
                help.configure(text="Press Space to Pause ")

            else:
                pause=True
                jeu.fenetre.after_cancel(id)
                lastX=snake.directionX
                lastY=snake.directionY
                snake.directionX=0
                snake.directionY=0
                jeu.canvas.create_text(jeu.width/2,jeu.height/3,fill="red",text="PAUSE",font=("arial",40,"bold"))
                help.configure(text="Press Space to Start ")
                
def dessiner():
    global jeu,snake,taille
    for i in range(len(snake.body)-1,-1,-1):
        queue=snake.body[i]
        if(i==0):
            queue[0]=snake.x
            queue[1]=snake.y
        else:
            prev_tile=snake.body[i-1]
            queue[0]=prev_tile[0]
            queue[1]=prev_tile[1]
    snake.x+=snake.directionX*taille
    snake.y+=snake.directionY*taille
    jeu.canvas.delete("all")
    jeu.canvas.create_rectangle(snake.x,snake.y,snake.x+taille,snake.y+taille,fill="#282")
    for queue in snake.body:
        jeu.canvas.create_rectangle(queue[0],queue[1],queue[0]+taille,queue[1]+taille,fill="yellow")
    jeu.canvas.create_rectangle(xPomme,yPomme,xPomme+taille,yPomme+taille,fill="red")
jeu=menu(400,500)
snake=Snake()
jeu.start()
jeu.fenetre.bind("<KeyPress>",changer)
jeu.fenetre.mainloop()