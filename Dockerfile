# Imagen base oficial de Python
FROM python:3.12-slim

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copio el script al contenedor
COPY contador.py /app/contador.py

# Al iniciar el contenedor ejecuto el script
CMD ["python", "contador.py"]
