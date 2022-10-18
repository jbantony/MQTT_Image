import paho.mqtt.client as mqtt
import time

MQTT_BROKER = "192.168.56.1" 
MQTT_TOPIC_1 = "Image/images"
MQTT_TOPIC_2 = "Image/commands"
CLEAN_SESSION = False
KEEP_ALIVE = 1200
PORT_ID = 1883
QOS_S = 1
QOS_P = 1
FILE_PATH = "C:\\Users\\Antony\\Downloads\\image_test.png"


def on_disconnect(client, userdata, flags, rc=0):
    m="DisConnected flags"+"result code "+str(rc)+"client:  "+str(client)
    print(m)

def on_connect(client, userdata, flags, rc):
    m="Connected flags"+str(flags)+"result code "+str(rc)+"client: "+str(client)
    print(m)

def pub(client, topic, msg, qos):
    client.publish(topic,msg,qos)

def sub(client, topic, qos):
    client.subscribe(topic, qos)

def data_convert(pub_file):
    f = open(pub_file, "rb")
    fileContent = f.read()
    byteArr = bytearray(fileContent)
    return byteArr

def on_message(client, userdata, message):
    msg=str(message.payload.decode("utf-8"))
    print(msg)


client = mqtt.Client("publisher_memory_test", clean_session=CLEAN_SESSION)
client.connect(MQTT_BROKER, PORT_ID, KEEP_ALIVE)
client.on_message = on_message

client.loop_start()
message = data_convert(FILE_PATH)

sub(client, MQTT_TOPIC_2, QOS_S)
time.sleep(2)

pub(client, MQTT_TOPIC_1, message, QOS_P)
time.sleep(2)

client.loop_stop()
client.disconnect()



