import json
import os

from fastapi import FastAPI, Request
from pydantic import BaseModel
from kafka import KafkaProducer

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "")
TOPIC_NAME = os.getenv("KAFKA_TOPIC", "")

print("🚀 Broker")
print(KAFKA_BROKER)
print(TOPIC_NAME)

app = FastAPI()
producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER,
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

class Message(BaseModel):
    msg: str

@app.post("/send")
async def send_message(message: Message):
    producer.send(TOPIC_NAME, {"message": message.msg})
    return {"status": "Message sent"}
