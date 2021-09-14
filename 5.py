import turtle as t

t.shape('turtle')
j=0
i=16
t.goto(0,0)
while i<160:
 while j<4:
  t.forward(i)
  t.left(90)
  j=j+1
 t.penup()
 t.goto(-i/2, -i/2)
 t.pendown()
 j=0
 i=i+16