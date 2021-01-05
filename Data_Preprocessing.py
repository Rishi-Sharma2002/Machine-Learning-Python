#IMPORTING THE LIBRARIES
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer

def main():
    os.system("clear")
    dataset = pd.read_csv("Data.csv")
    
    x = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values
    print(x)
    print(y)
main()



