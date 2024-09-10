import json
import random
import time
from utils import connect_mqtt, publish
from constants import TSEND, MQTT_TOPIC

if __name__ == "__main__":
    client = connect_mqtt()
    client.loop_start()

    while True:
        temperature = random.uniform(0, 100)
        humidity = random.uniform(0, 100)
        soilMoistureL1 = random.uniform(0, 100)
        soilMoistureL2 = random.uniform(0, 100)
        soilMoistureL3 = random.uniform(0, 100)
        soilMoistureL4 = random.uniform(0, 100)
        waterLevel = random.uniform(0, 100)
        pumpStatus = random.choice([0, 1])
        payload = {
            "Temperatura": temperature,
            "Humedad": humidity,
            "HumedadN1": soilMoistureL1,
            "HumedadN2": soilMoistureL2,
            "HumedadN3": soilMoistureL3,
            "HumedadN4": soilMoistureL4,
            "Nivel": waterLevel,
            "EstadoBomba": pumpStatus,
        }
        publish(client, MQTT_TOPIC, json.dumps(payload))
        time.sleep(TSEND)
