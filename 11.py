import turtle as t
import numpy as np
t.shape('turtle')
a=50
while a < 120:
 t.left(90)
 t.circle(a)
 t.circle(-a)
 t.right(90)
 a = a + 10