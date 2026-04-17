import pandas as pd

def runPreprocess(data, is_train=True):


    # Limpiar datos nan | Clean data nan
    if is_train:
        data = data.dropna(subset=[
            "Kicker_Foot",
            "Kicker_Side",
            "Home_Goals",
            "Away_Goals",
            "Minute",
            "Team_Type"
        ])
    else:
        data = data.dropna(subset=[
            "Kicker_Foot",
            "Home_Goals",
            "Away_Goals",
            "Minute",
            "Team_Type"
        ])

    # Eliminar la clase "C" de Kicker_Side ya que es muy poco representada y puede generar ruido en el modelo | Remove the "C" class from Kicker_Side since it is very underrepresented and can generate noise in the model
    if is_train:
        data = data[data["Kicker_Side"] != "C"]

    # Crear variable de diferencia de goles | Create goal difference variable
    data["Goal_Diff"] = data["Home_Goals"] - data["Away_Goals"]
    # Ajustar para visitantes | Adjust for away teams
    data.loc[data["Team_Type"] == "A", "Goal_Diff"] *= -1

    # Mapear datos | Map data
    data["Kicker_Foot"] = data["Kicker_Foot"].map({
        "R": 0,
        "L": 1
    })

    if is_train:
        data["Kicker_Side"] = data["Kicker_Side"].map({
            "R": 0,
            "L": 1,
        })
    data["Team_Type"] = data["Team_Type"].map({
        "H": 1,
        "A": 0
    })

    # Si el minuto es 45 o menos, lo marco como 0 y si es mayor a 45, lo marco como 1. | If the minute is 45 or less, I mark it as 0 and if it is greater than 45, I mark it as 1.
    data["Minute"] = (data["Minute"] > 45).astype(int)
    #data["Foot_vs_Side"] = data["Kicker_Foot"] == data["Kicker_Side"]

    # Seleccionar características y target | Select features and target
    features = [
        "Kicker_Foot",
        "Goal_Diff",
        "Minute",
        "Team_Type"
    ]

    x = data[features]
    

    if is_train:
        y = data["Kicker_Side"]
        return x, y
    else:
        return x