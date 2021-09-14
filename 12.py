import turtle as t
import numpy as np
t.shape('turtle')
a=1
t.penup()
t.goto(-100,0)
t.pendown()
while a< 10:
 t.left(90)
 t.circle(-50, 180)
 t.circle(-10,180)
 t.right(90)
 a=a+1