import pandas as pd
import sys
sys.path.append('./src')
from data.EDA import runEDA
from train import runTrain
from predict import runPredict



# ------------- DATA LOAD --------------

# Cargar datos | Load data
#data = pd.read_csv('data/data.csv')

dataPredict = {
    "Kicker_Foot": "R",
    "Home_Goals": 0,
    "Away_Goals": 0,
    "Minute": 42,
    "Team_Type": "H"
}

result = runPredict(dataPredict)
print("Prediccion:", result)
#runTrain()
#runEDA(data)

