import os
import random

from dotenv import load_dotenv

load_dotenv()

# MQTT_BROKER = "localhost"
MQTT_BROKER = os.environ.get("MQTT_BROKER") or "mqtt.dis.eafit.edu.co"
MQTT_PORT = os.environ.get("MQTT_PORT") or 1883
MQTT_CLIENT_ID = f"python-mqtt-{random.randint(0, 1000)}"
MQTT_USERNAME = os.environ.get("MQTT_USERNAME")
MQTT_PASSWORD = os.environ.get("MQTT_PASSWORD")
MQTT_TOPIC = os.environ.get("MQTT_TOPIC") or "/cultivo-iot2"
MQTT_FIRST_RECONNECT_DELAY = os.environ.get("MQTT_FIRST_RECONNECT_DELAY") or 1
MQTT_RECONNECT_RATE = os.environ.get("MQTT_RECONNECT_RATE") or 2
MQTT_MAX_RECONNECT_COUNT = os.environ.get("MQTT_MAX_RECONNECT_COUNT") or 12
MQTT_MAX_RECONNECT_DELAY = os.environ.get("MQTT_MAX_RECONNECT_DELAY") or 60
TSEND = os.environ.get("TSEND") or 1
