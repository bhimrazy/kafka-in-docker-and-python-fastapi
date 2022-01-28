import os
import json
from enum import Enum
from time import sleep
from kafka import KafkaConsumer

class EnvironmentVariables(str, Enum):
    KAFKA_TOPIC_NAME = 'KAFKA_TOPIC_NAME'
    KAFKA_SERVER = 'KAFKA_SERVER'
    KAFKA_PORT = 'KAFKA_PORT'

    def get_env(self, variable=None):
        return os.environ.get(self, variable)

# channel
topic = 'app'
# consumer
consumer = KafkaConsumer(topic, bootstrap_servers=f'{EnvironmentVariables.KAFKA_SERVER.get_env()}:{EnvironmentVariables.KAFKA_PORT.get_env()}', auto_offset_reset='latest', value_deserializer=lambda x: json.loads(x.decode('utf-8')))


def write_to_file(file, value):
    with open(f"{file}.json", "r+") as file:
        data = json.load(file)
        data['data'].append(value)
        file.seek(0)
        json.dump(data, file)


for message in consumer:
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                         message.offset, message.key, message.value))
    if message.key == b'create_product':
        write_to_file(file="product", value=message.value)
        print("Product written to file successfuly.")

    if message.key == b'create_data':
        write_to_file(file="data", value=message.value)
        print("Data written to file successfuly.")
