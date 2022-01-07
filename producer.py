
import json
from time import sleep
from kafka import KafkaProducer

# channel
topic = 'quickstart'

# producer
producer = KafkaProducer(bootstrap_servers=[
                         'localhost:9092'], value_serializer=lambda x: json.dumps(x).encode('utf-8'))

def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)

def on_send_error(excp):
    log.error('I am an errback', exc_info=excp)
    # handle exception

def publish(method: str, body: dict):
    producer.send(topic, key=method, value=body).add_callback(on_send_success).add_errback(on_send_error)

    # block until all async messages are sent
    producer.flush()