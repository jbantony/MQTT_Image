"""
Code to publish using normal client connection


"""
import paho.mqtt.client as mqtt
import time

MQTT_SERVER= "192.168.56.1" 
#MQTT_SERVER="test.mosquitto.org"
MQTT_PATH = "Image"

def on_publish(mosq, userdata, mid):
    mosq.disconnect()

client = mqtt.Client("publisher_test")
client.connect(MQTT_SERVER, 1883, 60)

client.on_publish = on_publish

client.loop_start()

f = open("C:\\Users\\Antony\\Downloads\\image_test.png", "rb")

fileContent = f.read()
byteArr = bytearray(fileContent)
client.publish(MQTT_PATH, byteArr, 0)

time.sleep(1)

client.loop_stop()

#client.loop_forever()
