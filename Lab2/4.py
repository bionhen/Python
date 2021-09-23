import turtle as t
import numpy as np
from random import *
t.shape('circle')
t.speed(100)
x = 0
y = 0
dt = 0.1
Vx = 10
Vy = 20
ay = -10
i = 0
while i < 1000:
 x += Vx*dt
 y += Vy*dt + ay*dt**2/2
 Vy += ay*dt
 i = i + 1
 if y < 0:
  Vy = -Vy
 t.goto(x, y)