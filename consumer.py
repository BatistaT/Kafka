from kafka import KafkaConsumer

TOPIC_NAME = 'games'

consumer = KafkaConsumer(TOPIC_NAME)

for message in consumer:
    print(message)