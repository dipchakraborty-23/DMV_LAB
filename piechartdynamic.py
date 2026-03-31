import matplotlib.pyplot as plt


n = int(input("Enter number of categories: "))

labels = []
sizes = []


for i in range(n):
    label = input(f"Enter label for category {i+1}: ")
    value = float(input(f"Enter value for {label}: "))
    
    labels.append(label)
    sizes.append(value)


plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)


plt.title("Pie Chart (User Input)")


plt.show()
