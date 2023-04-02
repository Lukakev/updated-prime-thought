from turtle import *
speed(200)
width(9)
forward(200)#bottom line
left(90)
forward(200)#right wall
left(90)
forward(200)#roof floor
left(90)
forward(200)#left wall
penup()
goto(200,200)#move to make roof
pendown()
left(210)
color("brown")
begin_fill()
forward(200)#roof
left(120)
forward(200)#roof
end_fill()
penup()
goto(200,90)#move200,90
pendown()
color("red")
right(60)
forward(60)#bottom of window
right(90)
forward(60)#window side

right(90)
forward(60)
right(90)
forward(60)
backward(60)
left(90)
backward(60)
color("blue")
backward(80)
color("red")
backward(60)
color("red")
left(270)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
color("blue")
backward(150)
right(90)
forward(80)
left(90)
forward(150)
backward(60)
left(90)
forward(10)
exitonclick()