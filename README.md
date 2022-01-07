# Kafka With Python
## Setup
```sh
    # Compose up
    $ docker-compose up -d

    # Getinto brocker bash
    $ docker exec -it broker bash

    # Create a topic with name quickstart
    $ kafka-topics --bootstrap-server broker:9092  --create  --topic quickstart

```
## Write messages to the topic
```sh
    # Getinto brocker bash
    $ docker exec -it broker bash

    # produce some message
    $ kafka-console-producer --bootstrap-server broker:9092  --topic quickstart
    > this is my first kafka message
    > hello world!
    > this is my third kafka message.

    # When you’ve finished, press Ctrl-D to return to your command prompt.

```
##  Read messages from the topic
```sh
    # Getinto brocker bash
    $ docker exec -it broker bash

    # produce some message
    $ kafka-console-consumer --bootstrap-server broker:9092  --topic quickstart --from-beginning

    # When you’ve finished, press Ctrl-C to return to your command prompt.

```
## Stop the Kafka broker
```sh
    # Stop containers
    $ docker-compose down
```
## Author
- [Bhimraj Yadav (@bhimrazy)](https://github.com/bhimrazy)

##🧾Resources
- [Apache Kafka® Quick Start](https://developer.confluent.io/quickstart/kafka-docker/)