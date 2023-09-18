#Turtle Party Project

import turtle

turtle.color('blue')

def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()
  
def move(len):
    back(len * -1)
  
def polygon(num, size):
  for i in range(num):
    turtle.forward(size)
    turtle.left(360 / num)

def spiral(len, angle):
  for i in range(len, 5, -4):
    turtle.forward(i)
    turtle.right(angle)
    
for n in range(3, 10):
  move(50)
  polygon(n, 100/n)
  back(50)
  turtle.right(360/7)
    
turtle.color('orange')
turtle.right(90)
move(100)
spiral(100, 90)
turtle.right(90)
move(80)
turtle.color('pink')
spiral(90, 60)
turtle.left(50)
move(250)
turtle.color('green')
for n in range(3, 12):
    move(50)
    polygon(n, 20)
    back(50)
    turtle.left(360/10)
turtle.left(120)
turtle.color('red')
move(180)
spiral(200, 200)
