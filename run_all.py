from src import generate_data
from src import cleaning
from src import modeling
from src import visualization

def main():
    print("Generando datos...")
    generate_data.main()
    
    print("Limpiando datos...")
    cleaning.main()
    
    print("Entrenando modelo...")
    modeling.main()
    
    print("Visualizando resultados...")
    visualization.main()

if __name__ == "__main__":
    main()
