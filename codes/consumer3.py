from kafka import KafkaConsumer
import json
import psycopg2
import logging
# Consumer configuration
try:
  consumer = KafkaConsumer('topic3',
                          bootstrap_servers=['kafka:9092'],
                          group_id='consumer-group-3',
                          auto_offset_reset='earliest',
                          value_deserializer=lambda v: json.loads(v.decode('utf-8')))
except Exception as e:
  logging.error(f'An error occured: {e}')

# Database connection details
dbname = "test"
dbuser = "root"
dbpassword = "12345"
dbhost = "localhost"
dbport = "5432"

def save_to_postgres(data):
  # Connect to Postgres database
  try:
    conn = psycopg2.connect(dbname=dbname, user=dbuser, password=dbpassword, host=dbhost, port=dbport)
    cur = conn.cursor()


    sql = f'''INSERT INTO users (
      id,
      first_name,
      last_name,
      location,
      gender,
      address, 
      postcode, 
      email, 
      username, 
      dob, 
      registered_date, 
      phone, 
      picture, 
      timestamp, 
      label) VALUES 
      (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    cur.execute(sql, (
    data["id"],
    data["first_name"], 
    data["last_name"],
    data["location"],
    data["gender"], 
    data["address"],
    data["postcode"],
    data["email"], 
    data["username"],
    data["dob"],
    data["registered_date"], 
    data["phone"],
    data["timestamp"],
    data["label"]))

    # Commit changes and close connection
    conn.commit()
    cur.close()
    conn.close()
    logging.info(f"Data saved to PostgreSQL database")
  except Exception as e:
    logging.error(f'An error occured: {e}')

# Loop to consume messages
for message in consumer:
  data = message.value
  save_to_postgres(data)

consumer.close()
