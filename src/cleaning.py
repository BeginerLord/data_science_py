import pandas as pd

def limpiar_datos(ruta_csv: str, ruta_salida: str) -> pd.DataFrame:
    # Cargar datos desde CSV y convertir la columna 'fecha' al tipo datetime
    df = pd.read_csv(ruta_csv, parse_dates=['fecha'])
    
    # Eliminar filas con valores nulos en campos críticos
    df = df.dropna(subset=['fecha', 'unidades_vendidas', 'precio_unitario'])
    
    # Extraer el año y el mes de la fecha para facilitar el análisis temporal
    df['anio'] = df['fecha'].dt.year  # Crear columna de año
    df['mes'] = df['fecha'].dt.month  # Crear columna de mes
    
    # Guardar los datos procesados en un nuevo archivo CSV
    df.to_csv(ruta_salida, index=False)
    print(f"Datos limpios guardados en {ruta_salida} con {len(df)} filas.")
    return df

def main():
    # Punto de entrada principal: limpia los datos desde la ubicación raw hasta la processed
    limpiar_datos('data/raw/ventas_simuladas.csv', 'data/processed/ventas_limpias.csv')

# Ejecuta la función main solo si este script se ejecuta directamente (no si se importa)
if __name__ == "__main__":
    main()