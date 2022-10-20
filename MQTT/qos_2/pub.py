import os
import paho.mqtt.client as mqtt
import time
import json
import base64

MQTT_BROKER = "192.168.56.1" 
MQTT_TOPIC_1 = "Image/images"
MQTT_TOPIC_2 = "Image/commands"
CLEAN_SESSION = False
KEEP_ALIVE = 1200
PORT_ID = 1883
QOS_S = 1
QOS_P = 1
FILE_PATH = "C:\\Users\\Antony\\Downloads\\"
FILE_NAME= "image_test.png"


def on_disconnect(client, userdata, flags, rc=0):
    m="DisConnected flags "+str(flags)+"result code "+str(rc)+" client:  "+str(client)
    print(m)

def on_connect(client, userdata, flags, rc):
    m="Connected flags"+str(flags)+"result code "+str(rc)+"client: "+str(client)
    print(m)

def pub(client, topic, msg, qos):
    result= client.publish(topic,msg,qos)
    return result

def sub(client, topic, qos):
    client.subscribe(topic, qos)

def data_to_json(pub_file):
    fileSize =  os.path.getsize(pub_file)
    filename = os.path.basename(pub_file)
    f = open(pub_file, "rb")
    fileContent = f.read()
    fileContent = base64.b64encode(fileContent)
    timeid = str(int(time.time()))
    payload = {
        "timeid": timeid,
        "filename": filename,
        "filesize": fileSize,
        "data": fileContent.decode(),
        "end": False
    }
    return json.dumps(payload)

def on_message(client, userdata, message):
    msg=str(message.payload.decode("utf-8"))
    print(msg)


client = mqtt.Client("publisher_memory_test", clean_session=CLEAN_SESSION)
client.on_message = on_message
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.connect(MQTT_BROKER, PORT_ID, KEEP_ALIVE)


client.loop_start()
message = data_to_json(FILE_PATH + FILE_NAME)

sub(client, MQTT_TOPIC_2, QOS_S)
time.sleep(1)

result = pub(client, MQTT_TOPIC_1, message, QOS_P)
print("Result:", result[0])
time.sleep(1)

client.loop_stop()
client.disconnect()



