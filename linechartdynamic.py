import matplotlib.pyplot as plt

n = int(input("Enter number of points: "))

x = []
y = []

for i in range(n):
    x.append(int(input(f"Enter x[{i}]: ")))
    y.append(int(input(f"Enter y[{i}]: ")))

plt.plot(x, y, marker='o')
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Line Chart (User Input)")
plt.show()