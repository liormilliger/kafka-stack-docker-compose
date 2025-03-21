import json
from kafka import KafkaConsumer, KafkaProducer
import threading

consumer = KafkaConsumer('topic1',
                         bootstrap_servers='kafka1:19092',
                         group_id='group1',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

producer = KafkaProducer(bootstrap_servers='kafka1:19092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def reply(message):
    response = {'reply': f'Got your message: {message}'}
    producer.send('topic2', response)
    print(f'Replied: {response}')

def consume_messages():
    for message in consumer:
        print(f'Consumed: {message.value}')
        reply(message.value)

if __name__ == "__main__":
    threading.Thread(target=consume_messages).start()
