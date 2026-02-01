# scaling : it ensure that all features contributes equally to the model
# by bringing them to a common scale,improving model performance
#for distance based algorithms. Z = (x-mean)/std.dev


from sklearn.preprocessing import StandardScaler
import numpy as np

X = np.array([[1, 2], [3, 4], [5, 6]])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print(X_scaled)