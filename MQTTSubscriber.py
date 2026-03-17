import paho.mqtt.client as mqtt
from iot_logger import get_mqtt_logger

# Initialize our custom logger
log = get_mqtt_logger("SUBSCRIBER")

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        log.info("Connected successfully.")
        client.subscribe("test/topic")
    else:
        log.error(f"Connection failed: {reason_code}")

def on_message(client, userdata, msg):
    log.info(f"Received message on {msg.topic}: {msg.payload.decode()}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.enable_logger(log) # Direct internal Paho logs to our file

log.info("Starting Subscriber...")
client.connect("localhost", 1883, 60)
client.loop_forever()