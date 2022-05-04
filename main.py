from turtle import *
from util import square, vector, cross
hideturtle()
tracer(False)
setup(880, 880, 150, 140)            # 빨간 줄 무시하세요
listen()
hideturtle()
square(-440, -430, 870, 'black')
square(-421, -411, 831, 'white')
for i in range (20) :
    square(-100+10*i, 180, 10, '#28036A')
    square(-180, -100+10*i, 10, '#28036A')

square(-100,-100,30,'red')
square(110,-100,20,'orange')
cross(130,-100,'blue')
done()