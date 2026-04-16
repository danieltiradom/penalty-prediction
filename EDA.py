import pandas as pd
#import seaborn as sns
import matplotlib.pyplot as plt

def runEDA(data):
    print("Data Head:")
    print(data.head())
    
    print("\nData Info:")
    print(data.info())
    
    print("\nData Description:")
    print(data.describe())


    print("\nRevisar valores unicos':")
    print("\n------Valores unicos de Kicker_Foot------:")
    print(data["Kicker_Foot"].unique())
    print(data["Kicker_Foot"].isna().sum())
    
    print("\n------Valores unicos de Kicker_Side------:")
    print(data["Kicker_Side"].unique())
    print(data["Kicker_Side"].isna().sum())
    print("\n------Valores unicos de Home_Goals------:")
    print(data["Home_Goals"].unique())
    print(data["Home_Goals"].isna().sum())
    print("\n------Valores unicos de Away_Goals------:")
    print(data["Away_Goals"].unique())
    print(data["Away_Goals"].isna().sum())
    print("\n------Valores unicos de Minute------:")
    print(data["Minute"].unique())
    print(data["Minute"].isna().sum())
    print("\n------Valores unicos de Team_Type------:")
    print(data["Team_Type"].unique())
    print(data["Team_Type"].isna().sum())
    
    
    """
    # Correlational matrix | Matriz de correlación
    plt.figure(figsize=(10, 8))
    sns.heatmap(data.corr(numeric_only=True), annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title("Correlation Matrix")
    plt.show()
    plt.close()
    """

    