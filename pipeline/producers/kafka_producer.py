# Author: Harshad Khetpal
from kafka import KafkaProducer
import json, logging, time, random, uuid
from datetime import datetime, timezone

class TransactionProducer:
    def __init__(self, bootstrap_servers="localhost:9092", topic="transactions"):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode(),
        )
        self.topic = topic

    def simulate_stream(self, n_events=10000):
        for i in range(n_events):
            tx = {
                "transaction_id": str(uuid.uuid4()),
                "customer_id": f"cust_{random.randint(1,10000):06d}",
                "amount": round(random.expovariate(0.01), 2),
                "timestamp": datetime.now(timezone.utc).isoformat(),
            }
            self.producer.send(self.topic, value=tx)
        self.producer.flush()
