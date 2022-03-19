# Kafka With Python

## Setup

[kafka.ipynb](https://github.com/bhimrazy/kafka-in-docker-and-python-fastapi/blob/main/kafka.ipynb) can be used to get hands on with kafka-python.

```sh
    # Compose up
    $ docker-compose up -d

    # Getinto kafka bash
    $ docker exec -it kafka bash

    # Create a topic with name quickstart
    $ kafka-topics --bootstrap-server kafka:9092  --create  --topic quickstart

    # list topics
    $ kafka-topics --list --bootstrap-server kafka:9092

```

## Write messages to the topic

```sh
    # Getinto kafka bash
    $ docker exec -it kafka bash

    # produce some message
    $ kafka-console-producer --bootstrap-server kafka:9092  --topic quickstart
    > this is my first kafka message
    > hello world!
    > this is my second kafka message.

    # When you’ve finished, press Ctrl-D to return to your command prompt.

```

## Read messages from the topic

```sh
    # Getinto kafka bash
    $ docker exec -it kafka bash

    # consume some message
    $ kafka-console-consumer --bootstrap-server kafka:9092  --topic quickstart --from-beginning

    # When you’ve finished, press Ctrl-C to return to your command prompt.

```

## Stop the Kafka broker

```sh
    # Stop containers
    $ docker-compose down
```

## Author

- [Bhimraj Yadav (@bhimrazy)](https://github.com/bhimrazy)

## 🧾Resources

- [Apache Kafka® Quick Start](https://developer.confluent.io/quickstart/kafka-docker/)
