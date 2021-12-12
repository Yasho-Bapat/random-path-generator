import turtle
import time
import random

number_of_loops = int(input("Enter number of loops: "))
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Turtle")
pointer = turtle.Turtle()

time.sleep(2)
for j in range(number_of_loops):
    turtle.resetscreen()
    for i in range(50):
        pointer.forward(20)
        turn = random.randint(0,1)
        if turn == 0:
            pointer.right(random.randint(0,135))
        elif turn == 1:
            pointer.left(random.randint(0,135))
        elif turn == 2:
            pointer.circle(random.randint(4, 10), 360)
        print(pointer.pos())

    #pointer.setheading(0)
    pointer.goto(0,0)

wn.exitonclick()
#time.sleep(10)