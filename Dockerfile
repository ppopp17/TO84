FROM python:2

# WORKDIR /bin
WORKDIR /src

ADD ./bin/* /bin/
ADD ./pythonConsumer/*.py /pythonConsumer/
ADD ./pythonConsumer/lib/*.py /pythonConsumer/lib/

RUN pip install kafka-python

ENV TOPIC_NAME=test
ENV CONSUMER_BOOTSTRAP=10.0.2.15:9092

# CMD [ "bash", "pythonConsumer.sh"]
CMD [ "python", "to84-consumer.py"]
