# MQTT Data Simulator

This is a simple MQTT data simulator that can be used to simulate data. The simulator is written in Python and uses the Paho MQTT client library to publish data to an MQTT broker.

## Installation

1. Clone the repository

2. Create a virtual environment and activate it

   ```bash
    python -m venv venv
    source venv/bin/activate
   ```

3. Install the required Python packages

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory of the project and add the following environment variables:

   ```bash
   MQTT_BROKER=YOUR_MQTT_BROKER
   MQTT_PORT=YOUR_MQTT_PORT
   MQTT_USERNAME=YOUR_MQTT_USERNAME
   MQTT_PASSWORD=YOUR_MQTT_PASSWORD
   MQTT_TOPIC=YOUR_MQTT_TOPIC
   MQTT_FIRST_RECONNECT_DELAY=DELAY
   MQTT_RECONNECT_RATE=RATE
   MQTT_MAX_RECONNECT_COUNT=COUNT
   MQTT_MAX_RECONNECT_DELAY=DELAY
   TSEND=TIME_INTERVAL
   ```

5. Run the simulator

   ```bash
   python app.py
   ```
