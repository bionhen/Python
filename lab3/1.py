import turtle as t
from random import *
t.shape('turtle')
i=0
t.speed(50)
for i in range (0, 400):
 t.forward(randint(10, 100))
 t.left(randint(0, 360))
 t.backward(randint(10, 100))
 t.right(randint(0, 360))
 i=i+1