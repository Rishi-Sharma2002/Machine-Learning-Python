#IMPORTING THE LIBRARIES
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer as si

def main():
    os.system("clear")
    dataset = pd.read_csv("Data.csv")
    
    x = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values
    print(x)
    print(y)
    imputer = si(missing_values=np.nan, strategy='median')
    imputer.fit(x[:, 1:3])
    x[:, 1:3]=imputer.transform(x[:, 1:3])
    os.system("clear")
    print(x)
main()



