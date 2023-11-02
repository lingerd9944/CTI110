import turtle
wn = turtle.Screen()
name = turtle.Turtle()

#Gets turtle and pen information 
name.pensize(2)            
name.pencolor("green")     
name.shape("turtle")

#setting variable for the loop
i = 0

#starting the single loop to write the letter "D"
while i < 1:
    name.left(90)
    name.forward(100)
    name.right(135)
    name.forward(50)
    name.right(30)
    name.forward(20)
    name.right(20)
    name.forward(20)
    name.right(50)
    name.forward(47)
    #adding 1 to the i variable to end the loop 
    i += 1   

#setting the turtle up to write the letter "L"
name.right(215)
name.penup()
name.forward(70)
name.pendown()

#Starting the write the letter "L"
name.left(90)
name.forward(100)
name.right(180)
name.penup()    #penup to not backtrack on the line
name.forward(100)
name.left(90)
name.pendown()   #pendown to start the bottom line of the letter "L"
name.forward(50)

#closing the program
wn.mainloop()