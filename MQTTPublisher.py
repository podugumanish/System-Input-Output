import paho.mqtt.client as mqtt
import time
from iot_logger import get_mqtt_logger

# Initialize our custom logger
log = get_mqtt_logger("PUBLISHER")

def on_publish(client, userdata, mid, reason_code, properties):
    log.info(f"Message Published (Mid: {mid})")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_publish = on_publish
client.enable_logger(log)

try:
    log.info("Attempting to send message...")
    client.connect("localhost", 1883, 60)
    client.loop_start()
    
    msg = "Hello from the unified logger!"
    status = client.publish("test/topic", msg, qos=1)
    status.wait_for_publish()
    
    log.info("Task finished.")
finally:
    client.loop_stop()
    client.disconnect()