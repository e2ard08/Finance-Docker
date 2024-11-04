# Utilizar una imagen base oficial de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo Python al contenedor
COPY Finance.py /app/Finance.py

# Instalar las dependencias
RUN pip install flask yfinance

# Exponer el puerto que usará la aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "Finance.py"]
