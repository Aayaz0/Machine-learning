from sklearn.model_selection import train_test_split
import numpy as np
x = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
y = np.array([0, 1, 0, 1])
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
print(f"X_train: {X_train.shape}, Test {X_test.shape}")