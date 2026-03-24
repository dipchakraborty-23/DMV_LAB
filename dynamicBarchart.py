import matplotlib.pyplot as plt

categories = []
values = []

n = int(input("How many categories do you want? "))

for i in range(n):
    category = input(f"Enter name of category {i + 1}: ")
    value = float(input(f"Enter value for {category}: "))

    categories.append(category)
    values.append(value)

plt.bar(categories, values)
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Chart using For Loop")
plt.show()