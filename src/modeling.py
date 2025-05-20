import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import joblib
import numpy as np
from sklearn.metrics import mean_squared_error
import os

def entrenar_modelo(ruta_csv: str, ruta_modelo: str):
    # Cargar datos procesados
    df = pd.read_csv(ruta_csv)
    
    # Seleccionar solo variables temporales como predictores
    # Esto aumenta la importancia de año y mes en el modelo
    X = df[['anio', 'mes']]
    y = df['unidades_vendidas']  # Variable objetivo a predecir

    # Dividir datos en conjuntos de entrenamiento (80%) y prueba (20%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Crear y entrenar modelo Random Forest con 100 árboles
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Asegurar que existe el directorio para guardar el modelo
    carpeta = os.path.dirname(ruta_modelo)
    if carpeta and not os.path.exists(carpeta):
        os.makedirs(carpeta)

    # Guardar modelo entrenado para uso posterior
    joblib.dump(model, ruta_modelo)
    print(f"Modelo guardado en {ruta_modelo}")

    # Realizar predicciones en conjunto de prueba
    y_pred = model.predict(X_test)

    # Calcular métricas de evaluación
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))  # Error cuadrático medio (raíz)
    r2 = r2_score(y_test, y_pred)  # Coeficiente de determinación

    # Mostrar métricas de desempeño del modelo
    print(f"RMSE: {rmse:.2f}")
    print(f"R²: {r2:.2f}")

    # Devolver modelo y datos para visualización posterior
    return model, X_test, y_test, y_pred

def main():
    # Función principal que ejecuta el entrenamiento del modelo
    entrenar_modelo('data/processed/ventas_limpias.csv', 'models/random_forest.joblib')

# Ejecutar solo cuando se llama directamente (no al importar)
if __name__ == "__main__":
    main()