import time
import json
from kafka import KafkaProducer
from kafka.errors import KafkaTimeoutError

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

def publish_message(producer):
    message = {'hello': 'world'}
    producer.send('topic1', message)
    print(f'Sent: {message}')

if __name__ == "__main__":
    producer = create_producer()
    while True:
        publish_message(producer)
        time.sleep(60)  # Send a message every minute
