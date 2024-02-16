import tensorflow as tf
import numpy as num
import pandas as pd

combo = pd.read_csv('data\\Combined_News_DJIA.csv')
data = pd.DataFrame(combo)
print(data.describe())
     