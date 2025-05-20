import pandas as pd
import numpy as np
import os

def generate_data():
    # Fijar semilla para reproducibilidad de datos aleatorios
    np.random.seed(42)
    # Crear rango de fechas mensuales desde 2019 hasta 2023
    fechas = pd.date_range(start='2019-01-01', end='2023-12-31', freq='ME')
    # Definir las tiendas disponibles para el análisis
    tiendas = ['Tienda A', 'Tienda B', 'Tienda C', 'Tienda D', 'Tienda E']
    # Definir categorías de productos
    categorias = ['Electrónica', 'Ropa', 'Alimentos', 'Juguetes']
    # Lista para almacenar todos los registros de ventas
    data = []

    for fecha in fechas:
        # Aplicar estacionalidad: incremento de ventas en último trimestre
        factor_mes = 1.0 + 0.2 * (fecha.month >= 10)  # 20% más de ventas en oct-dic
        # Aplicar tendencia creciente anual
        factor_anio = 1.0 + 0.1 * (fecha.year - 2019)  # 10% más cada año
        
        for tienda in tiendas:
            for categoria in categorias:
                # Generar unidades vendidas con distribución Poisson afectada por factores temporales
                unidades_vendidas = np.random.poisson(lam=50 * factor_mes * factor_anio)
                # Generar precios aleatorios uniformes entre 10 y 500
                precio_unitario = round(np.random.uniform(10, 500), 2)
                # Añadir registro a la lista de datos
                data.append({
                    'fecha': fecha,
                    'tienda': tienda,
                    'categoria': categoria,
                    'unidades_vendidas': unidades_vendidas,
                    'precio_unitario': precio_unitario
                })

    # Convertir lista de diccionarios a DataFrame
    df = pd.DataFrame(data)
    
    # Asegurar que existe el directorio para guardar datos
    os.makedirs('data/raw', exist_ok=True)
    
    # Guardar datos simulados en CSV
    df.to_csv('data/raw/ventas_simuladas.csv', index=False)
    print("CSV generado en data/raw/ventas_simuladas.csv")
    return df

def main():
    # Función principal que ejecuta la generación de datos
    generate_data()

# Punto de entrada del script cuando se ejecuta directamente
if __name__ == "__main__":
    main()