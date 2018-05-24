from kafka import KafkaConsumer
import sys
import time

class TO84KafkaConsumer(object):
    def __init__(self,topicName,bootstrapServers):
        self.consumer = KafkaConsumer(topicName,bootstrap_servers=[bootstrapServers]);

    def listen(self):
        for message in self.consumer:
            currentTicks = time.time()
            print ("%s:%d:%d: key=%s value=%s time=%.6f" % (message.topic, message.partition,
                                                  message.offset, message.key,
                                                  message.value, currentTicks))
            sys.stdout.flush()
