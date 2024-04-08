import turtle             
win = turtle.Screen()      
t = turtle.Turtle()    

i = 0

while i < 4:
    t.forward(100)
    t.left(90)
    i = i + 1



t.penup()
t.forward(150)
t.pendown() 

i = 0

while i < 3: 
    t.forward(100)          
    t.left(120)            
    i = i + 1
    
    
    

win.mainloop()
    
