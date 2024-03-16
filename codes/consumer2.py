from kafka import KafkaConsumer, KafkaProducer
import json
import random
import logging

# List of labels
labels = ["label1", "label2", "label3"]

# Consumer configuration
try:
  consumer = KafkaConsumer('topic2',
                          bootstrap_servers=['kafka:9092'],
                          group_id='consumer-group-2',
                          auto_offset_reset='earliest',
                          value_deserializer=lambda v: json.loads(v.decode('utf-8')))


  # Loop to consume messages
  for message in consumer:
    data = message.value
    data["label"] = random.choice(labels)

# Send data to topic "topic3"

  producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
                            value_serializer=lambda v: json.dumps(v).encode('utf-8'))
  producer.send('topic3', data)
  producer.flush()

  logging.info(f"Data with random label sent to topic: topic3")
except Exception as e:
  logging.error(f'An error occured: {e}')

  producer.close()

consumer.close()
