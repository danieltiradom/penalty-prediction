import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def runEDA(data):
    print("Data Head:")
    print(data.head())
    
    print("\nData Info:")
    print(data.info())
    
    print("\nData Description:")
    print(data.describe())
    
    # Correlational matrix | Matriz de correlación
    plt.figure(figsize=(10, 8))
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
