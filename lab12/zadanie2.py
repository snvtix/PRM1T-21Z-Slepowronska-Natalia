import matplotlib.pyplot as plt
import math
import numpy


y=[]
x=range(-10,11)
for i in x:
    y.append(i**2)

plt.plot(x,y)
plt.title("wykres f(x)=x**2")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()


y=[]
x=numpy.linspace(0,2*math.pi)
for i in x:
    y.append(numpy.sin(i))

plt.plot(x,y)
plt.title("wykres f(x)=sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()



kolo=plt.Circle((0.5,0.5), 0.2, color="blue")
fig,ax=plt.subplots()
plt.title("wykres kola")
plt.xlabel("x")
plt.ylabel("y")
ax.set_aspect("equal")
ax.plot()
ax.add_patch(kolo)
plt.grid()
plt.show()





