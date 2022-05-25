import random
import time
from paho.mqtt import client as mqtt_client

broker = 'broker.emqx.io'
port = 1883
topic = "/askisi3"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        client.publish(topic, msg)
        print(f"Send {msg} to topic `{topic}`")
        msg_count += 1


client = connect_mqtt()
client.loop_start()
publish(client)