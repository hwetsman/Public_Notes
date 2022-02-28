Necessary when features are unbalanced in min-max range.
x` is new feature
calculate x` by x-x<sub>min</sub> divided by xmax-xmin

sklearn requires floats for MinMaxScaler:

`from sklearn.preprocessing import MinMaxScaler
import numpy as np
weights = np.array([[100.0],[110.0],[150.0]])
scaler = MinMaxScaler()
rescaled_weights = scaler.fit_transform(weights)
