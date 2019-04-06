import turtle as t
import math as m
setbutton=(("0"," ",".","Del","=","Clr"),("1","2","3","*","^3","^(1/3)"),("4","5","6","-","^2","^(1/2)"),("7","8","9","+","/","!"),("","","","","",""),("","","","","",""),("","","","","",""),("","","","","",""))
def button(x,y):
    if(x>5 or y>5):return
    global result,temp
    x=int(x)
    y=int(y)
    if((x==0 and y==0) or (x<=3 and x>=1 and y<=2 and y>=0) or (x==0 and y==2)):
        result+=setbutton[x][y]
        temp+=setbutton[x][y]
        
    if(setbutton[x][y]=="Clr"):
        result=""
        temp=""
    if(setbutton[x][y]=="Del" and len(result)>0):
        result = result[:-1]
        temp = temp[:-1]
    if(setbutton[x][y]=="+" or setbutton[x][y]=="-" or setbutton[x][y]=="*" or setbutton[x][y]=="/"):
        result=""
        temp=str(eval(temp))
        temp+=setbutton[x][y]

    t.clear()
    cal()
    t.up()
    t.goto(-125,200)
    t.down()
    t.pencolor("black")
    
    if(setbutton[x][y]=="!"):
        t.write(int(m.gamma(int(eval(temp))+1)),font=("Arial",40))
        temp=str(int(m.gamma(int(eval(temp))+1)))
        result=temp
    if(setbutton[x][y]=="^2"):
        t.write(float(eval(temp))**2,font=("Arial",40))
        temp=str(float(eval(temp))**2)
        result=temp
    if(setbutton[x][y]=="^3"):
        t.write(float(eval(temp))**3,font=("Arial",40))
        temp=str(float(eval(temp))**3)
        result=temp
    if(setbutton[x][y]=="^(1/3)"):
        t.write(float(eval(temp))**(1/3),font=("Arial",40))
        temp=str(float(eval(temp))**(1/3))
        result=temp
    if(setbutton[x][y]=="^(1/2)"):
        t.write(float(eval(temp))**(1/2),font=("Arial",40))
        temp=str(float(eval(temp))**(1/2))
        result=temp
    
    
    if(setbutton[x][y]=="="):
        t.write(eval(temp),font=("Arial",40))
        temp=str(eval(temp))
        result=temp
    else:t.write(result,font=("Arial",40))
    print(temp)
    t.update()
def pos(x,y):
    x//=60
    y+=30
    y//=60
    x+=3
    y+=4
    button(y,x)
    print(y,x)
def cal():
    t.pencolor("black")
    t.up()
    t.goto(0,0)
    t.down()
    t.setheading(0)
    t.bgcolor("silver")
    t.width(3)
    t.up()
    t.fd(200)
    t.down()
    t.lt(90)
    t.fd(300)
    t.lt(90)
    t.fd(400)
    t.lt(90)
    t.fd(600)
    t.lt(90)
    t.fd(400)
    t.lt(90)
    t.fd(300)
    t.up()
    x=-210
    y=-240
    t.pencolor("white")
    for i in range(7):
        for k in range(6):
            t.pencolor("white")
            x+=60
            t.goto(x,y)
            t.dot(50)
            t.pencolor("black")
            xx=x-16
            yy=y-16
            t.goto(xx,yy)
            t.write(setbutton[i][k],font=("Arial",20))
        y+=60
        x=-210
    t.pencolor("white")
    t.width(100)
    t.up()
    t.goto(-125,220)
    t.setheading(0)
    t.down()
    t.fd(250)
    t.up()
t.tracer(False)
temp=""
result=""
t.hideturtle()
cal()
t.update()
t.listen()
t.onscreenclick(pos,1)
