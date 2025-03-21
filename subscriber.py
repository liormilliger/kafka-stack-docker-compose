import json
import time
from kafka import KafkaConsumer, KafkaProducer
from kafka.errors import KafkaTimeoutError
import threading

def create_consumer():
    consumer = None
    while consumer is None:
        try:
            print("Creating Kafka Consumer...")
            consumer = KafkaConsumer(
                'topic1',
                bootstrap_servers='kafka1:19092',  # Define the Kafka broker
                group_id='group1',
                value_deserializer=lambda x: json.loads(x.decode('utf-8'))
            )
            print("Kafka Consumer created successfully.")
        except KafkaTimeoutError:
            print("Failed to connect to Kafka. Retrying...")
            time.sleep(5)  # Wait before retrying
    return consumer

def create_producer():
    producer = None
    while producer is None:
        try:
            print("Creating Kafka Producer...")
            producer = KafkaProducer(
                bootstrap_servers='kafka1:19092',  # Define the Kafka broker
                value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )
            print("Kafka Producer created successfully.")
        except KafkaTimeoutError:
            print("Failed to connect to Kafka. Retrying...")
            time.sleep(5)  # Wait before retrying
    return producer

def reply(message, producer):
    response = {'reply': f'Got your message: {message}'}
    producer.send('topic2', response)
    print(f'Replied: {response}')

def consume_messages(consumer, producer):
    for message in consumer:
        print(f'Consumed: {message.value}')
        reply(message.value, producer)

if __name__ == "__main__":
    consumer = create_consumer()
    producer = create_producer()
    threading.Thread(target=consume_messages, args=(consumer, producer)).start()