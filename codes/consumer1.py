from kafka import KafkaConsumer, KafkaProducer
import json
from datetime import datetime
import logging

# Consumer configuration
try:
  consumer = KafkaConsumer('topic1',
                          bootstrap_servers=['kafka:9092'],
                          group_id='consumer-group-1',
                          auto_offset_reset='earliest',
                          value_deserializer=lambda v: json.loads(v.decode('utf-8')))

  # Loop to consume messages
  for message in consumer:
    data = message.value
    data["timestamp"] = datetime.utcnow().isoformat()

  # Send data to topic "topic2"
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                              value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    producer.send('topic2', data)
    producer.flush()
    logging.info(f"Data with timestamp sent to topic: topic2")
    
except Exception as e:
  logging.error(f'An error occured: {e}')

  

  producer.close()

consumer.close()
