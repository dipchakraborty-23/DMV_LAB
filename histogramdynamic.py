import matplotlib.pyplot as plt

n = int(input("Enter number of values: "))
data = []

for i in range(n):
    data.append(int(input(f"Enter value {i+1}: ")))

plt.hist(data, bins=5)
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Histogram (User Input)")
plt.show()
