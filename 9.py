import turtle as t
import numpy as np
t.shape('turtle')
def Polyg(n):
 t.penup()
 t.forward(20*n)
 t.pendown()
 i=0
 t.left(180-180*(n-2)/(2*n))
 t.forward(40 * n * np.sin(np.pi / n))
 while i < n-1:
  t.speed(1)
  t.left(360/n)
  t.forward(40*n*np.sin(np.pi/n))
  i=i+1
 t.right(90*(n-2)/n)
 t.penup()
 t.backward(20*n)
 t.pendown()
j=3
while j<11:
 Polyg(j)
 j=j+1
