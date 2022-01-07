import json
from time import sleep
from kafka import KafkaConsumer

#consumer
consumer = KafkaConsumer(topic, bootstrap_servers=['localhost:9092'],auto_offset_reset='earliest',value_deserializer=lambda x:json.loads(x.decode('utf-8')))

for message in consumer:
    message = message.value
    print('Message :{}'.format(message))