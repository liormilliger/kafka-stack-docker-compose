import time
import json
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='kafka1:19092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def publish_message():
    message = {'hello': 'world'}
    producer.send('topic1', message)
    print(f'Sent: {message}')

if __name__ == "__main__":
    while True:
        publish_message()
        time.sleep(60)
