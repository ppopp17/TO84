from kafka import KafkaConsumer
import sys

class TO84KafkaConsumer(object):
    def __init__(self,topicName,bootstrapServers):
        self.consumer = KafkaConsumer(topicName,bootstrap_servers=[bootstrapServers]);

    def listen(self):
        for message in self.consumer:
            print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                                  message.offset, message.key,
                                                  message.value))
            sys.stdout.flush()
