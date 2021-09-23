from random import randint
import turtle as t
import numpy as np
t.shape('circle')
t.penup()
t.goto(-200, -200)
t.pendown()
t.speed(50)
for g in range(4):
 t.forward(400)
 t.left(90)
number_of_turtles = 20
steps_of_time_number = 1000000
pool = [t.Turtle(shape='circle') for i in range(number_of_turtles)]
Vx = [randint(-20,20) for l in range(number_of_turtles)]
Vy = [((-1)**randint(0, 10))*np.sqrt(400-(Vx[k])**2) for k in range(number_of_turtles)]
x = [randint(-200, 200) for k in range(number_of_turtles)]
y = [randint(-200, 200) for k in range(number_of_turtles)]
print(Vx, Vy)
for unit in pool:
    unit.penup()
    unit.speed(0.5)
for i in range(steps_of_time_number):
    for j in range(number_of_turtles):
        pool[j].goto(x[j], y[j])
        x[j] += Vx[j]*0.1
        y[j] += Vy[j]*0.1
        if x[j] < -200 or x[j] > 200:
             Vx[j] = -Vx[j]
        if y[j] < -200 or y[j] > 200:
             Vy[j] = -Vy[j]

