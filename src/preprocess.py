import pandas as pd

def runPreprocess(data):


    # Limpiar datos nan | Clean data nan
    data = data.dropna(subset=[
        "Kicker_Foot",
        "Kicker_Side",
        "Home_Goals",
        "Away_Goals",
        "Minute",
        "Team_Type"
    ])

    # Mapear datos | Map data
    data["Kicker_Foot"] = data["Kicker_Foot"].map({
        "R": 0,
        "L": 1
    })
    data["Kicker_Side"] = data["Kicker_Side"].map({
        "R": 1,
        "L": 0,
        "C": 2
    })
    data["Team_Type"] = data["Team_Type"].map({
        "H": 1,
        "A": 0
    })

    # Seleccionar características y target | Select features and target
    features = [
        "Kicker_Foot",
        "Home_Goals",
        "Away_Goals",
        "Minute",
        "Team_Type"
    ]

    x = data[features]
    y = data["Kicker_Side"]

    return x, y