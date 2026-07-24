import json
import time
import random
import paho.mqtt.client as mqtt


client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2
)


client.connect(
    "localhost",
    1883,
    60
)


while True:

    data = {

        "device": "coffee-machine-001",

        "temperature": round(
            random.uniform(20,30), 2
        ),

        "humidity": random.randint(40,70),

        "waterLevel": random.randint(0,100),

        "coffeeLevel": random.randint(0,100),

        "wifi": random.randint(-70,-40),

        "heartbeat": 1
    }


    client.publish(
        "coffee/telemetry",
        json.dumps(data)
    )


    print(data, flush=True)

    time.sleep(5)

