#IMPORTING THE LIBRARIES
import os
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer as si 
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder

def main():
# Reading the dataset
  dataset = pd.read_csv("Data.csv")
  x = dataset.iloc[:,:-1].values
  y = dataset.iloc[:, -1].values
  print(x)
  print(y)

# Compling the missing values
  impute = si(missing_values=np.nan, strategy='mean')
  x[:, 1:3] = impute.fit_transform(x[:, 1:3])

  os.system("clear")
  print(x)
  Encoder(x, y)

#Encoding the values
def Encoder(x, y):
  os.system("clear")
  ct = ColumnTransformer(transformers=[("encoder", OneHotEncoder(), [0])], remainder="passthrough")
  x = np.array(ct.fit_tranform(x))
  le = LabelEncoder()
  y = le.fit_transform(y)
  print(x)
  print(y)
  


if __name__ == "__main__":
  main()

