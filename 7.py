import turtle as t

t.shape('turtle')
a=0.2
i=0
t.goto(0,0)
while i < 2160:
 t.speed(100)
 t.forward(a)
 t.left(1)
 i = i + 1
 a=a+0.001
