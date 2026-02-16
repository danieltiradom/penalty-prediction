import pandas as pd
from EDA import *

data = pd.read_csv('data/raw_data.csv')

runEDA(data)