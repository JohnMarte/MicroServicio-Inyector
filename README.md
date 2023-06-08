# MicroServicio-Inyector
esta es la traza del error 

   File "/Productor/productorKafka.py", line 42, in <module>
     ejecutar_cada_30_segundos()
   File "/Productor/productorKafka.py", line 37, in ejecutar_cada_30_segundos
     ejecutar_programa()
  File "/Productor/productorKafka.py", line 14, in ejecutar_programa
     producer = KafkaProducer(bootstrap_servers='kafka:9092')
   File "/usr/local/lib/python3.10/site-packages/kafka/producer/kafka.py", line 381, in __init__
    client = KafkaClient(metrics=self._metrics, metric_group_prefix='producer',
   File "/usr/local/lib/python3.10/site-packages/kafka/client_async.py", line 244, in __init__
     self.config['api_version'] = self.check_version(timeout=check_timeout)
   File "/usr/local/lib/python3.10/site-packages/kafka/client_async.py", line 900, in check_version
     raise Errors.NoBrokersAvailable() 
