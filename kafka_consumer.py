from kafka import KafkaConsumer
import csv
import json

consumer = KafkaConsumer('test1', bootstrap_servers='localhost:9092', auto_offset_reset='earliest')

def save_csv(data):
    try:
        # Split the CSV-like data into values
        values = data.strip().split(',')
        values = [value.strip('"') for value in data.strip().split(',')]
        print(values)
        
        # Open the CSV file in append mode
        with open('kafka_data.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(values)
                
    except Exception as e:
        print(f"Error: {e}")

try:
    for message in consumer:
        consumed_data = message.value.decode()  
        save_csv(consumed_data)
except KeyboardInterrupt:
    consumer.close()
