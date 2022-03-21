import turtle
turtle.speed(10)       #画笔速度
turtle.width(4)        #画笔的粗细
color=("red","green","blue","black")
for x in range(3):     #0 1 2 3 4
    turtle.penup()   #先抬笔
    turtle.goto(0,-x*100)  #走笔
    turtle.down()         #放笔
    turtle.color(color[x%4])  #画笔颜色
    turtle.circle((x+1)*100) #画⚪


turtle.done()   #执行完窗口依然在