# To publish the MQTT Message

import paho.mqtt.client as paho
from paho import mqtt
from time import sleep
import random

# define static variable
# broker = "localhost" # for local connection
broker = "broker.emqx.io"  # for online version
port = 1883
timeout = 60

username = ''
password = ''
topic = "sic-mqtt/data_dummy"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_publish(client,userdata,result):
	print("data published \n")



client1 = paho.Client("device1",userdata=None,protocol=paho.MQTTv5)
client1.username_pw_set(username=username,password=password)
client1.on_connect = on_connect
client1.on_publish = on_publish
client1.connect(broker,port,timeout)

count = 0
#ingin forever loop
# while True:
while count < 5:
	data = int(random.random()*100)
	ret = client1.publish(topic,payload=data,qos=1)
	print("data sent")
	sleep(1)