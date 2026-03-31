import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y_line = [10, 20, 15, 25, 30]
y_bar = [5, 7, 3, 8, 6]

fig, axs = plt.subplots(1, 2, figsize=(10, 4))

axs[0].plot(x, y_line, marker='o', color='blue')
axs[0].set_title("Line Graph")
axs[0].set_xlabel("X values")
axs[0].set_ylabel("Y values")

axs[1].bar(x, y_bar, color='orange')
axs[1].set_title("Bar Graph")
axs[1].set_xlabel("X values")
axs[1].set_ylabel("Y values")

plt.tight_layout()

plt.show()
