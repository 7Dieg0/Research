
import turtle
#learn to import turtle system

turtle.setup(650, 350, 200, 200) 
#set up a canvas
turtle.penup()
#brush raised
turtle.fd(-250)
#tutle start to reverse 250, but no marks
turtle.pendown()
#The brush falls and begins to draw
turtle.pensize(25)
turtle.pencolor("purple") 
#Adjust the size and colour of the turtles
turtle.seth(-40)
#start to move (drawing)
for i in range(4):
    turtle.circle(40, 80) 
    turtle.circle(-40, 80) 
#4 loops start
turtle.circle(40, 80/2)
turtle.fd(40)
#drawing neck
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
#drawing head
turtle.done()
#The program will not automatically exit after running


#Pretty cool，like that @_@
