import pandas as pd
#from EDA import runEDA
import sys
sys.path.append('./src')
from train import runTrain

# ------------- DATA LOAD --------------

# Cargar datos | Load data
data = pd.read_csv('data/data.csv')


runTrain()
#runEDA(data)

