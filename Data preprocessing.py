# 1st step is to import important libraries:
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer

def main():
    os.system("cls")
    dataset = pd.read_csv('D:\OneDrive - srmist.edu.in\Coding\Machine Learning\Data.csv')
    x = dataset.iloc[:,:-1].values
    y = dataset.iloc[:,-1].values
    print(x)
    print(y)
    imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
    imputer.fit(x[:, 1:3])
    x[:, 1:3]=imputer.transform(x[:, 1:3])
    print(x)

main()
