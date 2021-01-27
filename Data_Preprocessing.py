#IMPORTING THE LIBRARIES
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer as si
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder

def encoding(x, y):
  os.system("clear")
  ct = ColumnTransformer(transformers=[
  ('encoder', OneHotEncoder(), [0])], remainder='passthrough')

  x = np.array(ct.fit_transform(x))
  #print(x)

  le = LabelEncoder()
  y = le.fit_transform(y)
  print(y)

def main():
    os.system("clear")
    dataset = pd.read_csv("Data.csv")

    x = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values
    print(x)
    print(y)
    imputer = si(missing_values=np.nan, strategy='mean')
    #imputer.fit(x[:, 1:3])
    x[:, 1:3]=imputer.fit_transform(x[:, 1:3])
    os.system("clear")
    print(x)
    #encoding(x, y)
main()



