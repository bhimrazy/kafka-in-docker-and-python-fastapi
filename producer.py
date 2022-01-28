import os
import json
from enum import Enum
from time import sleep
from kafka import KafkaProducer

class EnvironmentVariables(str, Enum):
    KAFKA_TOPIC_NAME = 'KAFKA_TOPIC_NAME'
    KAFKA_SERVER = 'KAFKA_SERVER'
    KAFKA_PORT = 'KAFKA_PORT'

    def get_env(self, variable=None):
        return os.environ.get(self, variable)


# channel
topic = 'app'

# producer
producer = KafkaProducer(
    bootstrap_servers=f'{EnvironmentVariables.KAFKA_SERVER.get_env()}:{EnvironmentVariables.KAFKA_PORT.get_env()}',
    value_serializer=lambda x: json.dumps(x).encode('utf-8'))


def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)

def on_send_error(excp):
    # log.error('I am an errback', exc_info=excp)
    # handle exception
    pass


def publish(method: str, body: dict):
    producer.send(topic, key=method.encode('UTF-8') ,value=body).add_callback(
        on_send_success).add_errback(on_send_error)
    print(f'Topic :{topic}  Key :{method}   published.')

    # block until all async messages are sent
    producer.flush()

