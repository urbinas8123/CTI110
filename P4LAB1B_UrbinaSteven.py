import turtle             
win = turtle.Screen()      
t = turtle.Turtle()


t.pencolor("green")
t.pensize(4)



t.penup()
t.goto(-50,50)
t.pendown()
t.setheading(0)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)


t.penup()
t.forward(150)
t.pendown()




t.right(90)
t.forward(50)
t.circle(50, 180)
t.forward(50)

win.mainloop()


