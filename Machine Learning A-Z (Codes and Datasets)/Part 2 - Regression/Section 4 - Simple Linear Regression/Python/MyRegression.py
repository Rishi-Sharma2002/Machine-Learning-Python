#Importing the libraries
import numpy as np
import pandas as pd

dataset = pd.read_csv("Salary_Data.csv")
x = dataset.iloc[:, : -1]
y = dataset.iloc[:, -1]

#Splitting the Training Set and Test Set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.2, random_state=0)

#Using Linear Regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)