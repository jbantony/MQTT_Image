"""
Code to publish single file, using absolute path, to the MQTT Mosquitto server with a topic 
    MQTT_SERVER = Server address of the local MQTT mosquitto broker, from the local IP
    MQTT_PATH   = The topic name to publish
"""

import paho.mqtt.publish as publish

MQTT_SERVER= "192.168.56.1" 
MQTT_PATH = "Image"


f = open("C:\\Users\\Antony\\Downloads\\image_test.png", "rb")
fileContent = f.read()
byteArr = bytearray(fileContent)

publish.single(MQTT_PATH, byteArr, qos=1, hostname=MQTT_SERVER, client_id="publisher_test2")
