# MicroServicio-Inyector
Esta es la traza del error:

   "Traceback (most recent call last):
  File "/Productor/productorKafka.py", line 79, in <module>
    ejecutar_programa()
  File "/Productor/productorKafka.py", line 18, in ejecutar_programa
    producer = KafkaProducer(bootstrap_servers='kafka:9092')
  File "/usr/local/lib/python3.10/site-packages/kafka/producer/kafka.py", line 381, in __init__
    client = KafkaClient(metrics=self._metrics, metric_group_prefix='producer',
  File "/usr/local/lib/python3.10/site-packages/kafka/client_async.py", line 244, in __init__
    self.config['api_version'] = self.check_version(timeout=check_timeout)
  File "/usr/local/lib/python3.10/site-packages/kafka/client_async.py", line 900, in check_version
    raise Errors.NoBrokersAvailable()
kafka.errors.NoBrokersAvailable: NoBrokersAvailable".
