import numpy as np
import matplotlib.pyplot as plt

x1 = np.random.rand(50) 

y1 = -x1 + np.random.normal(0, 0.1, 50)

x2 = np.random.uniform(0.1, 0.3, 10)
y2 = np.random.uniform(0.5, 0.7, 10)

x_outlier = np.array([0.9])
y_outlier = np.array([1.5])

x = np.concatenate([x1, x2, x_outlier])
y = np.concatenate([y1, y2, y_outlier])

plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', alpha=0.7, label='Data Points')

plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Scatter Plot: Negative Correlation, Clusters, and Outliers')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

plt.show()