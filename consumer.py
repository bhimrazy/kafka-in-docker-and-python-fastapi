import os
import json
from enum import Enum
from time import sleep
from kafka import KafkaConsumer

# channel
topic = 'app'

# consumer
consumer = KafkaConsumer(topic, bootstrap_servers=[
                         'localhost:9092'], auto_offset_reset='latest', value_deserializer=lambda x: json.loads(x.decode('utf-8')))


def write_to_file(file, value):
    with open(f"{file}.json", "r+") as file:
        data = json.load(file)
        data['data'].append(value)
        file.seek(0)
        json.dump(data, file)


for message in consumer:
    print("Consuming.....")
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                         message.offset, message.key, message.value))
    if message.key == b'create_product':
        write_to_file(file="product", value=message.value)
        print("Product written to file successfuly.")

    if message.key == b'create_data':
        write_to_file(file="data", value=message.value)
        print("Data written to file successfuly.")
