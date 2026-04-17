import joblib
import pandas as pd
from src.preprocess import runPreprocess

def runPredict(dataPredict):
    
    #Convertiir a DataFrame | Convert to DataFrame
    data = pd.DataFrame([dataPredict])

    # Preprocesar datos | Preprocess data
    x = runPreprocess(data, is_train=False)

    # Cargar modelo y scaler | Load model and scaler
    model = joblib.load('models/model.pkl')
    scaler = joblib.load('models/scaler.pkl')

    # Escalar datos | Scale data
    numeric_cols = ["Goal_Diff", "Minute"]
    x[numeric_cols] = scaler.transform(x[numeric_cols])

    # Realizar predicción | Make prediction
    prediction = model.predict(x)

    if prediction[0] == 0:
        return "Derecha"
    else:
        return "Izquierda"