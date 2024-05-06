from kafka import KafkaProducer
import json
import time
import random
from faker import Faker

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

topic_name = 'test1'
fake = Faker()

while True:
    
    co2_data = {
        'source': random.choice(['Factory', 'Vehicle', 'Power Plant', 'Agriculture', 'Construction', 'Shipping', 'Deforestation']),
        'co2_level': random.randint(300, 1000),  # 300 and 1000 ppm
        'location': fake.country(),  
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
    }
    
    csv_like_data = f"{co2_data['source']},{co2_data['co2_level']},{co2_data['location']},{co2_data['timestamp']}"
    
    producer.send(topic_name, value=csv_like_data)
    print(f"Produced: {csv_like_data}")
    time.sleep(3)

producer.close()
