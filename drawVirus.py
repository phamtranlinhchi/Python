from turtle  import *
from time import *
color('green')
bgcolor('black')
speed(11)
hideturtle()
b = -100
while b < 200:
	right(b)
	forward(b * 3)
	b = b + 1
sleep(2)