# To publish the MQTT Message

import paho.mqtt.client as mqtt
# from paho import mqtt
from time import sleep
import random

# define static variable
# broker = "localhost" # for local connection
# broker = "things.ubidots.com"  # for online version
broker = "industrial.api.ubidots.com"  # for online version
# broker = "broker.emqx.io"  # for online version
port = 1883
timeout = 60

username = ''
password = ''
topic = "/v1.6/devices/mentor_ham/temperature"


def connect_mqtt() -> mqtt:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt.Client()
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

client = connect_mqtt()
client.loop_start()
count = 0
#ingin forever loop
# while True:
while count < 5:
	temp = int(random.random()*100)
	send_message = str({"value":temp})
	client.publish(topic,payload=send_message,qos=0, retain=False)
	print("send message "+send_message)
	sleep(1)
	count = count + 1
