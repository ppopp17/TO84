import os
import sys
from kafka import KafkaConsumer
from kafka_consumer.to84_kafka_consumer import TO84KafkaConsumer
from utilities.environment import TO84Environment

#print "Entered main..."
#sys.stdout.flush()

#topicName = os.environ['TOPIC_NAME']
#bootstrapServers = os.environ['CONSUMER_BOOTSTRAP']

#print "Topic ="+topicName+", broker="+bootstrapServers
#sys.stdout.flush()

env = TO84Environment()

TO84_Consumer = TO84KafkaConsumer(env.topicName,env.bootstrapServers)
#print "KafkaConsumer created"
#sys.stdout.flush()
#TO84_Consumer = TO84KafkaConsumer('test','10.0.2.15:9092')
TO84_Consumer.listen()
