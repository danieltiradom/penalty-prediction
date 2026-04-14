import pandas as pd
from EDA import *

# ------------- DATA LOAD --------------

# Cargar datos | Load data
data = pd.read_csv('data/data.csv')



runEDA(data)