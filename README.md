## PEC 1 - Despliegue y Escalabilidad

Este repositorio contiene la solución a la PEC 1 del Máster en Data Science (UAH).
El proyecto consiste en un contador en Python desplegado en Kubernetes mediante Docker.

### Estructura
- **contador.py:** script que cuenta del 1 al 10. con **time.sleep(60)**
- **Dockerfile**: Contenedor para empaquetar el script.
- **deployment.yaml**: Configuración para desplegar 3 réplicas en Kubernetes en estado Runing

### Instrucciones de ejecución
Para desplegar este proyecto localmente es necesario construir la imagen antes, ya que el deployment busca la imagen en local:

1. Construir la imagen Docker:
   ```bash
   docker build -t contador-pec1:1.0 .
