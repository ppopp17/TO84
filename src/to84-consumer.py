import os
import sys
from kafka import KafkaConsumer
from lib.to84_kafka_consumer import TO84KafkaConsumer

print "Entered main..."
sys.stdout.flush()

topicName = os.environ['TOPIC_NAME']
bootstrapServers = os.environ['CONSUMER_BOOTSTRAP']

print "Topic ="+topicName+", broker="+bootstrapServers
sys.stdout.flush()

TO84_Consumer = TO84KafkaConsumer(topicName,bootstrapServers)
print "KafkaConsumer created"
sys.stdout.flush()
#TO84_Consumer = TO84KafkaConsumer('test','10.0.2.15:9092')
TO84_Consumer.listen()
