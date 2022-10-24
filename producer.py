from kafka import KafkaProducer

TOPIC_NAME='games'
KAFKA_SERVER = 'localhost:9092'

messages = ['God of War Ragnarok', 'The Last of Us Part 2', 'A Plage Tale: Requiem', 'Elden Ring']

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

for game in messages:
    data = bytes(game,'UTF-8')

    producer.send(TOPIC_NAME, value=data)
    producer.flush()
