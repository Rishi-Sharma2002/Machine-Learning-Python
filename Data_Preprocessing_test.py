#Importing the libraries
import numpy as np
import pandas as pd
#Taking Care of missing data
from sklearn.impute import SimpleImputer as si
# Doing OneHotEncoding
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder

def encoder(x, y):
    ct = ColumnTransformer(transformers=[
        ('encoder', OneHotEncoder(), [0])], remainder='passthrough')
    x = np.array(ct.fit_transform(x))
    print(x)
    le = LabelEncoder()
    y = le.fit_transform(y)
    print(y)


def missing_data(x, y):
    imputer = si(missing_values=np.nan, strategy="mean")
    x[:, 1:3] = imputer.fit_transform(x[:, 1:3])
    print(x)
    encoder(x, y)



def read_data():
    dataset = pd.read_csv("Data.csv")
    x = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values
    missing_data(x, y)

if __name__=="__main__":
    read_data()