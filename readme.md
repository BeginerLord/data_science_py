# Proyecto Ciencia de Datos - Modelo Predictivo de Ventas

## Descripción

Este proyecto consiste en desarrollar un modelo predictivo que permita anticipar las unidades vendidas de productos utilizando variables temporales (año y mes).  
Se simulan datos con patrones estacionales y tendencias anuales para entrenar un modelo Random Forest y evaluar su desempeño.

---

## Requisitos y dependencias

Para ejecutar este proyecto es necesario contar con Python 3.x instalado y las siguientes librerías:

- pandas
- numpy
- scikit-learn
- joblib
- matplotlib
- seaborn

---

## Instalación

1. **Clonar el repositorio** (si aplica):

```bash
git clone <url-del-repositorio>
cd <nombre-del-proyecto>
Crear y activar entorno virtual (recomendado):

bash
Copy
Edit
python -m venv venv
# Windows
venv\Scripts\activate

Instalar dependencias:

bash
Copy
Edit
pip install -r requirements.txt
Estructura del proyecto
data/: Carpeta con datos simulados y procesados.

src/: Código fuente dividido en módulos para generación, limpieza, modelado y visualización.

models/: Carpeta donde se guarda el modelo entrenado.

requirements.txt: Archivo con las dependencias del proyecto.

run_all.py: Script maestro para ejecutar el pipeline completo.

Uso
Para ejecutar todo el flujo de trabajo, activar el entorno virtual y correr:

bash
python run_all.py