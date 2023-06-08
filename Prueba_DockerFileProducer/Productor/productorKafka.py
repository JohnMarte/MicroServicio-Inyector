import os
import pandas as pd
from kafka import KafkaProducer
import schedule
import time

def ejecutar_programa():
    # ruta de la carpeta que contiene los archivos CSV
    carpeta_archivos = "./ApiCoches/"

    # lista todos los archivos en la carpeta
    archivos = os.listdir(carpeta_archivos)

    # filtrar solo los archivos CSV
    archivos_csv = [archivo for archivo in archivos if archivo.endswith(".csv")]

    # configuracion del producer de kafka
    producer = KafkaProducer(bootstrap_servers=['kafka:9092'],api_version=(0,1,0))

    # iterar sobre todos los archivos CSV en la carpeta
    for archivo_csv in archivos_csv:
        # construir la ruta completa del archivo CSV
        ruta_archivo = os.path.join(carpeta_archivos, archivo_csv)

        # cargar los datos del archivo CSV en un DataFrame
        datos = pd.read_csv(ruta_archivo)

        # Calcular el tamaño de cada parte
        tam_parte = len(datos) // 4

        # Dividir los datos en cuatro partes
        datos1 = datos.iloc[:tam_parte]
     
        datos2 = datos.iloc[tam_parte:tam_parte*2]
        datos3 = datos.iloc[tam_parte*2:tam_parte*3]
        datos4 = datos.iloc[tam_parte*3:]
        
        # Convertir DataFrames a JSON
        json_data1 = datos1.to_json(orient="records")
        
        json_data2 = datos2.to_json(orient="records")
        json_data3 = datos3.to_json(orient="records")
        json_data4 = datos4.to_json(orient="records")
        
        # Asignando nombre del topic
        topic = "kafka_prueba"

        print("paso antes de enviar")
        # Enviar los datos a través de Kafka
        future1 = producer.send(topic, value=json_data1.encode('utf-8'))
        future2 = producer.send(topic, value=json_data2.encode('utf-8'))
        future3 = producer.send(topic, value=json_data3.encode('utf-8'))
        future4 = producer.send(topic, value=json_data4.encode('utf-8'))
       
        # Confirmación de entrega
      
        print("paso despuessssss de enviar")
        producer.flush()
        print(f'Datos del archivo {archivo_csv} enviados.')

    # cerrar el productor de Kafka
    producer.close()


def ejecutar_diariamente():
    ejecutar_programa()
    # Programar la ejecución del programa cada 24 horas
    schedule.every(24).hours.do(ejecutar_programa)

#ejecutar el programa por privera vez
ejecutar_diariamente()

while True:
    # Ejecutar las tareas programadas
    schedule.run_pending()
    time.sleep(1)
