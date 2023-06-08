# Establecer la imagen base de Python
FROM python:3.10

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /Productor

# Copiar los archivos necesarios al contenedor
COPY productorKafka.py ./
COPY ApiCoches ./ApiCoches
COPY requirements.txt ./

# Instalar las dependencias del programa
RUN pip install -r requirements.txt

# Comando para ejecutar el script Python dentro del contenedor
CMD ["python","productorKafka.py"]