# Utiliza una imagen base de Python 3.9 slim
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de la aplicación al contenedor
COPY . .

# Instalar las dependencias
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto para Flask
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
