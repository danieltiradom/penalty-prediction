import pandas as pd
import joblib

from preprocess import runPreprocess
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix



def runTrain():
    # Cargar y procesar datos | Load and process data
    data = pd.read_csv('data/data.csv')
    x, y = runPreprocess(data)

    # Dividir datos en entrenamiento y prueba | Split data into training and testing
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=49, stratify=y)

    # Escalar variables numericas (Esto sirve para "igualar" la importancia de las variables) | Scale numerical variables (This helps to "equalize" the importance of the variables)
    # Solo escalo estas variables, y no las categoricas (Kicker_Foot, Team_Type) ya que no representan una magnitud, sino una categoria | I only scale these variables, and not the categorical ones (Kicker_Foot, Team_Type) since they do not represent a magnitude, but a category
    scaler = StandardScaler()

    numeric_cols = ["Goal_Diff", "Minute"]

    x_train[numeric_cols] = scaler.fit_transform(x_train[numeric_cols])
    x_test[numeric_cols] = scaler.transform(x_test[numeric_cols])

    # Crear y entrenar el modelo | Create and train the model
    model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

    model.fit(x_train, y_train)

    # Evaluar el modelo | Evaluate the model
    y_pred = model.predict(x_test)
    print(classification_report(y_test, y_pred))

    print("Value counts of target variable in training set:")
    print(y.value_counts())

    print("Matriz de confusión:")
    print(confusion_matrix(y_test, y_pred))


if __name__ == "__main__":
    runTrain()