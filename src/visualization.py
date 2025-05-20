import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
import os

def graficar_importancia(model, features):
    # Extraer importancia de características del modelo
    importancias = model.feature_importances_
    
    # Convertir features a lista de strings para evitar problemas en el eje Y
    if hasattr(features, 'tolist'):
        features = features.tolist()
    
    features_str = [str(f) for f in features]  # Convertir a string
    
    # Mostrar valores exactos para debugging y análisis
    for f, imp in zip(features_str, importancias):
        print(f"Característica: {f}, Importancia: {imp:.6f}")
    
    # Crear gráfico de barras para visualizar importancia
    plt.figure(figsize=(12, 8))
    sns.barplot(x=importancias, y=features_str)
    plt.title('Importancia de las variables')
    
    # Añadir etiquetas con los valores exactos para mejor interpretación
    for i, v in enumerate(importancias):
        plt.text(v + 0.01, i, f"{v:.4f}", va='center')
        
    plt.tight_layout()
    plt.show()  # Mostrar gráfico en ventana interactiva

def graficar_predicciones(y_test, y_pred):
    # Crear gráfico de dispersión para comparar valores reales vs predichos
    plt.figure(figsize=(12, 8))
    plt.scatter(y_test, y_pred, alpha=0.3)  # Puntos semi-transparentes
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')  # Línea diagonal de referencia
    plt.xlabel('Valores reales')
    plt.ylabel('Valores predichos')
    plt.title('Predicción vs Real')
    plt.tight_layout()
    plt.show()  # Mostrar gráfico en ventana interactiva

def cargar_datos_y_predecir(ruta_csv, ruta_modelo):
    # Cargar datos procesados y modelo entrenado
    df = pd.read_csv(ruta_csv)
    model = joblib.load(ruta_modelo)

    # Coherente con el cambio en modeling.py, solo usamos año y mes como predictores
    X = df[['anio', 'mes']]
    y = df['unidades_vendidas']  # Variable objetivo: unidades vendidas

    # Dividir datos usando la misma semilla que en entrenamiento para consistencia
    _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Generar predicciones con el modelo entrenado
    y_pred = model.predict(X_test)

    return model, X_test, y_test, y_pred

def main():
    # Rutas a archivos de datos y modelo
    ruta_csv = 'data/processed/ventas_limpias.csv'
    ruta_modelo = 'models/random_forest.joblib'

    print("Cargando datos y modelo...")
    model, X_test, y_test, y_pred = cargar_datos_y_predecir(ruta_csv, ruta_modelo)
    
    print("Generando gráfico de importancia de variables...")
    graficar_importancia(model, X_test.columns)
    
    print("Generando gráfico de predicciones vs valores reales...")
    graficar_predicciones(y_test, y_pred)

# Ejecutar visualizaciones solo cuando se llama directamente
if __name__ == "__main__":
    main()