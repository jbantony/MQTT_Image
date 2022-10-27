import paho.mqtt.client as mqtt
import time
import json, base64

MQTT_BROKER = "192.168.56.1" 
MQTT_TOPIC_1 = "Image/images"
MQTT_TOPIC_2 = "Image/commands"
CLEAN_SESSION = False
KEEP_ALIVE = 1200
PORT_ID = 1883
QOS_S = 1
QOS_P = 1
List_sub_message = []



def on_disconnect(client, userdata, flags, rc=0):
    m= "DisConnected with flags: "+"  Result code: "+str(rc)+"  Client:  "+str(client)
    print(m)

def on_connect(client, userdata, flags, rc):
    m= "Connected with flags: "+str(flags)+"  Result code: "+str(rc)+"  Client: "+str(client)
    print(m)

def pub(client, topic, msg, qos):
    client.publish(topic,msg,qos)

def sub(client, topic, qos):
    client.subscribe(topic, qos)

def json_to_data(msg):
    # Convert JSON message to its original form
    msg= msg.decode()
    msg = json.loads(msg)
    img_data = base64.b64decode(msg["data"])
    print("Recived data ", msg["filename"],  "Data Size: ", msg["filesize"])
    name = msg["timeid"] + "_"+ msg["filename"]
    #print(name)
    f = open(name, "wb")
    f.write(img_data)
    print("Image Saved as ", name)
    f.close()
    # Add the filename to the list of messages
    List_sub_message.append(msg["filename"])
   

def on_message(client, userdata, msg):
    json_to_data(msg.payload)
    print("Totally {} data received" .format(len(List_sub_message)))
    pub(client, MQTT_TOPIC_2, "New data received: "+List_sub_message[-1], 1 )
    

client = mqtt.Client("image_subscriber", clean_session=CLEAN_SESSION)
client.connect(MQTT_BROKER, PORT_ID, KEEP_ALIVE)
client.on_connect = on_connect
client.on_message = on_message


sub(client, MQTT_TOPIC_1, QOS_S)
time.sleep(2)

pub(client, MQTT_TOPIC_2, "message", QOS_P)
time.sleep(2)

client.loop_forever()



