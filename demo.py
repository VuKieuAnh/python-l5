import turtle

t = turtle.Turtle()

width=200
height=100

t.forward(width)
t.right(90)
t.forward(height)
t.right(90)
t.forward(width)
t.right(90)
t.forward(height)
turtle.done()

if(a > b):
    if(a > c):
        print ("Greatest number is a = " + a)
    else:
        print ("Greatest number is c = " + c)
else:
    if(b > c):
        print ("Greatest number is b = " + b)
    else:
        print ("Greatest number is c = " + c)
