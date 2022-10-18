import cv2
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from PIL import Image
import PIL.ImageOps
import os, ssl, time


# fetching data from  image.npz
X = np.load('image.npz')['arr_0']
y = pd.read_csv("labels.csv")['labels']

print(pd.Series(y).value_counts())
classes = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
           'Q','R','S','T','U','V','W','X','Y','Z']
nclasses = len(classes)


# #Splitting the data and scaling it
# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=9, train_size=, test_size=)
# #scaling the features
# X_train_scaled = X_train/255.0
# X_test_scaled = X_test/255.0

