import turtle as t

t.shape('turtle')
a=15
i=0
t.goto(0,0)
while i < 100:
 t.speed(5)
 t.forward(a)
 t.left(90)
 i = i + 1
 a=a+5