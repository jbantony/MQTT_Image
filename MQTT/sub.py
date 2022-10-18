########## Workflow ############
"""  


doc: https://stackoverflow.com/questions/37499739/how-can-i-send-a-image-by-using-mosquitto 
Ref: Eclipse: https://github.com/eclipse/paho.mqtt.python/issues/369 

1. In a terminal: "mosquitto -v -c mosquitto.conf" -> Starts the mosquitto
     conf file of mosquitto: http://www.steves-internet-guide.com/mosquitto-broker/ 

2. Run the sub.py
    This will recive the image and save it


3. Run the pub.py in a new terminal, where paho is installed -> python pub.py
    pub.py is having the image file configured


 """
####################################

from cgi import test
from tokenize import Number
import paho.mqtt.client as mqtt
import os
import time

#MQTT_SERVER = "localhost"

#MQTT_SERVER= "test.mosquitto.org"

MQTT_SERVER = "192.168.56.1" 
MQTT_PATH = "Image"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH)
    # The callback for when a PUBLISH message is received from the server.


def on_message(client, userdata, msg):
    # more callbacks, etc
    # Create a file with write byte permission
    #os.chdir("test\\")
    name = time.strftime("%H%M%S")
    name= "output"+name+".jpg"
    f = open(name, "wb")
    #f = open('output.jpg', "wb")
    f.write(msg.payload)
    print("Image Received", time.ctime())
    f.close()

client = mqtt.Client("subscriber_test")

client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
try:
    client.loop_forever()

except KeyboardInterrupt:
    client.disconnect()
    exit(0)