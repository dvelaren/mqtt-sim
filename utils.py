import time
import paho.mqtt.client as mqtt

from constants import (
    MQTT_BROKER,
    MQTT_CLIENT_ID,
    MQTT_FIRST_RECONNECT_DELAY,
    MQTT_MAX_RECONNECT_COUNT,
    MQTT_MAX_RECONNECT_DELAY,
    MQTT_PASSWORD,
    MQTT_PORT,
    MQTT_RECONNECT_RATE,
    MQTT_USERNAME,
)


def connect_mqtt():
    def on_connect(client, userdata, flags, rc, properties=None):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    def on_disconnect(client, userdata, rc):
        print("Disconnected with result code: %s", rc)
        reconnect_count, reconnect_delay = 0, MQTT_FIRST_RECONNECT_DELAY
        while reconnect_count < MQTT_MAX_RECONNECT_COUNT:
            print("Reconnecting in %d seconds...", reconnect_delay)
            time.sleep(reconnect_delay)

            try:
                client.reconnect()
                print("Reconnected successfully!")
                return
            except Exception as err:
                print("%s. Reconnect failed. Retrying...", err)

            reconnect_delay *= MQTT_RECONNECT_RATE
            reconnect_delay = min(reconnect_delay, MQTT_MAX_RECONNECT_DELAY)
            reconnect_count += 1
        print("Reconnect failed after %s attempts. Exiting...", reconnect_count)

    client = mqtt.Client(
        client_id=MQTT_CLIENT_ID, callback_api_version=mqtt.CallbackAPIVersion.VERSION2
    )
    client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.connect(MQTT_BROKER, MQTT_PORT)
    return client


def publish(client, topic, payload):
    result = client.publish(topic, payload)
    status = result[0]
    if status == 0:
        print(f"Send `{payload}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")
    return status
