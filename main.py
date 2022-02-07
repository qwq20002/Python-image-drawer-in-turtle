import turtle
import cv2

pic=cv2.imread(r"in.jpg")
size = pic.shape

turtle.setup(len(pic[0]),len(pic[1]),0,0)
turtle.colormode(255)
turtle.speed(0)
turtle.delay(0)
turtle.tracer(False)
turtle.penup()
turtle.setpos(-400,300)
turtle.pendown()
for i in range(size[0]):
    for j in range(size[1]):
        turtle.pencolor(pic[i,j][2],pic[i,j][1],pic[i,j][0])
        turtle.forward(1)
    turtle.penup()
    turtle.setpos(-400,300-i)
    turtle.pendown()
