import random
from paho.mqtt import client as mqtt_client

broker = 'broker.emqx.io'
port = 1883
topic = "/askisi3"
client_id = f'python-mqtt-{random.randint(0, 100)}'

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"We received {msg.payload.decode()} from `{msg.topic}`")

    client.subscribe(topic)
    client.on_message = on_message


client = connect_mqtt()
subscribe(client)
client.loop_forever()