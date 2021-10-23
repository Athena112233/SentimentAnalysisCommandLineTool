import pandas as pd
import pyspark
import pickle

train = pd.read_csv("../data/train.csv")
test = pd.read_csv("../data/test.csv")

print("Peak data: ")
print(train.head(10))

print("See label breakdown: ")
print(train.label.value_counts())