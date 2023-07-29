# Subscriber (To Receive The Message )

import paho.mqtt.client as mqtt

# define static variable
# broker = "localhost" # for local connection
broker = "broker.emqx.io"  # for online version
port = 1883
timeout = 60

username = ''
password = ''

topic = "SIC_Message/Test"
# format topic: Nemuu/Camera_Data
#               MVR/Curtain_Status
# mau subscribe semua topic: #

# The callback for when the client receives a CONNACK response from the server.
# fungsi ini digunakan untuk connect ke broker MQTT sesuai settingan
def connect_mqtt() -> mqtt:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt.Client()
    # client.username_pw_set(username, password) #for Broker with password
    client.on_connect = on_connect
    # print("test")
    client.connect(broker, port)
    return client

# The callback for when a PUBLISH message is received from the server.
# Fungsi ini digunakan untuk menangkap message yang masuk ke broker dan ingin disubscribe
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload.decode('utf-8')))
    payload_decoded = msg.payload.decode('utf-8')
    if payload_decoded == "On":
        print("Lampu dinyalakan")
        # Do something

    elif payload_decoded == "Off":
        print("Lampu dimatikan")
        # Do something else

    elif payload_decoded == "sens"
        print("read sensor value")
        # Do something else
        
    else:
        print("perintah tidak di kenali")

print("Connecting to broker ...")
client = connect_mqtt()

print("Creating new MQTT client ...")
client.on_message = on_message

# subscribe to all topic
# apabila ingin difilter topic nya, bisa diubah di bagian ini
print("Subscribing to topics ...")
client.subscribe(topic)

client.loop_forever()