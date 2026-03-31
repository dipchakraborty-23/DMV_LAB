import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5, 6]
y = [10, 15, 13, 17, 20, 22]


plt.scatter(x, y, color='green', marker='o')


plt.title("Simple Scatter Plot")
plt.xlabel("X values")
plt.ylabel("Y values")

plt.grid(True)

plt.show()
