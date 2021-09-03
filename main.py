import pandas
from sklearn.linear_model import LinearRegression
data = pandas.read_csv("price.csv")
model = LinearRegression()
model.fit(data[['version']], data[['price']])
print(model.predict([[11]]))
print(model.predict([[12]]))
print(model.predict([[13]]))
print(model.predict([[14]]))
print(model.predict([[15]]))