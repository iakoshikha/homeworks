from turtle import *


#we want to paint a house

shape ("turtle")
#draw a square
#speed(20)
width(7)
color("pink")
forward (200)
left(90)

forward (200)
left(90)

forward (200)
left(90)

forward (200)
left(90)

#end of square

#drawing a door

forward (70)
color("yellow")
left(90)
forward(120)
right(90)
forward(60) 
right(90)
forward(120)

penup()
goto(200,200)
pendown()

color("orange")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


#drawig a window
width(4)
color ("pink")

penup()
goto(120,200)
pendown()

left (30)
forward (60)
left(90)
forward(79)
left(90)
forward (60)

penup()
goto(161,200)
pendown()

right(180)
forward(57)

penup()
goto(161,175)
pendown()

right (90)
forward (40)

penup()
goto(161,175)
pendown()

right(180)
forward (39)

penup()
goto(85,200)
pendown()

right(90)
forward(59)

right(90)
forward(82)

right(90)
forward(59)

penup()
goto(43,200)
pendown()

right(180)
forward(59)

penup()
goto(43,175)
pendown()

right(90)
forward(40)

penup()
goto(43,175)
pendown()

left(180)
forward(40)

penup()
goto(110,60)
pendown()



exitonclick()

