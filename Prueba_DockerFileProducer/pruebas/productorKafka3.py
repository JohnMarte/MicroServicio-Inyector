import pandas as pd
from kafka import KafkaProducer
import schedule
import time


# ruta del archivo CSV que quieres leer
ruta_archivo = "./ApiCoches/hyundai.csv"

# cargar los datos del archivo CSV en un DataFrame
datos = pd.read_csv(ruta_archivo)

# configuracion del producer de kafka
producer = KafkaProducer(bootstrap_servers='kafka:9092')

# coger solo las 100 primeras filas
df_100 = datos.iloc[:10]

# Convertir DataFrames a JSON
json_data1 = df_100.to_json(orient="records")

# asignando nombre del topic
topic = "kafka_prueba"

# enviar los datos atraves de kafka
producer.send(topic, value=json_data1.encode('utf-8'))

# confirmación de entrega
producer.flush()
print('Datos enviados.')

# cerrar el productor de Kafka
producer.close()

