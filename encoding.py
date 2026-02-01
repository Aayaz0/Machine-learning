from sklearn.preprocessing import LabelEncoder
date = ['red', 'blue', 'red', 'blue']
le = LabelEncoder()
encoded = le.fit_transform(date)
print(encoded)