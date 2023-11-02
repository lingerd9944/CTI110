import turtle
wn = turtle.Screen()
shape = turtle.Turtle()

#Putting in pen and turtle information 
shape.pensize(2)            
shape.pencolor("green")     
shape.shape("turtle")

#Assigning a variable for the loop 
i = 0 

#Starting the loop for one rotation to draw the triangle
while i < 1: 
    shape.forward(100)          
    shape.left(120)            
    shape.forward(100)
    shape.left(120)
    shape.forward(100)
    #adding one to the 'i' variable to end the loop on the next pass
    i += 1

#Setting up the turtle to start drawing the sqaure
shape.penup()
shape.left(30)
shape.forward(100)
shape.pendown()

#Turtle starts drawing the sqaure
shape.forward(50)          
shape.left(90)             
shape.forward(50)
shape.left(90)
shape.forward(50)
shape.left(90)
shape.forward(50)

#ending the program
wn.mainloop()