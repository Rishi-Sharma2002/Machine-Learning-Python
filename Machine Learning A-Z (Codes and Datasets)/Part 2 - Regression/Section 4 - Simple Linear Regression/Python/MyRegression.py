#importing the libraries
import numpy as np
import pandas as pd

#reading the dataset
dataset = pd.read_csv("Salary_Data.csv")
x = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]

#Splitting the dataset in Training and Test
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Strating with LinearRegression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)
