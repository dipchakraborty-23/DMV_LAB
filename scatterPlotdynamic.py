import matplotlib.pyplot as plt

data=input("Enter the values:")
y=list(map(int,data.split()))
x=range(0,len(y))
plt.scatter(x, y, color='red', marker='o')

plt.title("Scatter Plot")
plt.xlabel("X values")
plt.ylabel("Y values")

plt.grid(True)

plt.show()
