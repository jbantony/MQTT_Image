'''
Code to publish multiple files in a folder in the pwd to the MQTT Mosquitto server with a topic 
    MQTT_SERVER = Server address of the local MQTT mosquitto broker, from the local IP
    MQTT_PATH   = The topic name to publish

'''

import paho.mqtt.publish as publish
import os
import time

MQTT_SERVER= "192.168.56.1" 

MQTT_PATH = "Image"


for root, dirs, file in os.walk("."):
    print("There are {} files in total".format(len(file)))
    for item in file:
        if item.endswith(('.jpg', '.png', 'jpeg')):
            f= open(item, "rb")
            fileContent = f.read()
            byteArr = bytearray(fileContent)

            publish.single(MQTT_PATH, byteArr, qos=1, hostname= MQTT_SERVER, client_id="publisher_test3")
            time.sleep(1)
            

