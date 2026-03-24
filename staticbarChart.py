import matplotlib.pyplot as plt
import numpy as np


categories = ['Apples', 'Bananas', 'Cherries', 'Dates']
sales = [450, 300, 200, 500]

plt.bar(categories, sales, color='skyblue') 


plt.title('Fruit Sales Data')
plt.xlabel('Fruits')
plt.ylabel('Sales')


plt.show()