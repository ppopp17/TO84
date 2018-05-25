from kafka import KafkaConsumer
import sys
import time

class TO84KafkaConsumer(object):
    def __init__(self,topicName,bootstrapServers):
        print("Topic=%s, broker=%s" % (topicName, bootstrapServers))
        sys.stdout.flush()
        #self.consumer = KafkaConsumer(topicName,bootstrap_servers=[bootstrapServers]);
        self.consumer = KafkaConsumer(topicName,bootstrap_servers=['10.0.2.15:9092','10.0.2.15:9093','10.0.2.15:9094']);

    def listen(self):
        for message in self.consumer:
            currentTicks = time.time()
            print ("%s:%d:%d: key=%s value=%s time=%.6f" % (message.topic, message.partition,
                                                  message.offset, message.key,
                                                  message.value, currentTicks))
            sys.stdout.flush()
