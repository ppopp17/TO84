FROM python:2

WORKDIR /src

#ADD ./bin/* /bin/
ADD ./src/*.py /src/
ADD ./src/kafka_consumer/*.py /src/kafka_consumer/

RUN pip install kafka-python

ENV TOPIC_NAME=test
ENV CONSUMER_BOOTSTRAP=10.0.2.15:9092

# CMD [ "bash", "src.sh"]
CMD [ "python", "to84-consumer.py"]
