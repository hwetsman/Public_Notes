## Ordinary Least Squares
sklearn.LinearRegression

`from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])`

`reg.score(train_x,train_y)` gives r squared
`reg.score(test_x,test_x)`
reg.predict(x) will give list of y's
slope = reg.coef_
intercept = reg.intercept_

## Gradient Descent
