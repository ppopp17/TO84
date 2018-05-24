import os

class TO84Environment(object):
    def __init__(self):
        self.topicName = os.environ['TOPIC_NAME']
        self.bootstrapServers = os.environ['CONSUMER_BOOTSTRAP']
