import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

x = []
y = []

fig, ax = plt.subplots()
ax.set_xlim(0, 20)
ax.set_ylim(0, 100)

line, = ax.plot([], [], marker='o')

def update(frame):
    x.append(frame)
    y.append(random.randint(0, 100))  
    line.set_data(x, y)
    return line,

ani = FuncAnimation(fig, update, frames=20, interval=300)

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Animated Line Chart with Random Values")
plt.show()
