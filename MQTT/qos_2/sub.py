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
List_sub_message = []



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

def on_message(client, userdata, msg):
    name = time.strftime("%H%M%S")
    name= "output"+name+".jpg"
    f = open(name, "wb")
    f.write(msg.payload)
    print("Image Received", time.ctime())
    f.close()
    List_sub_message.append(True)
    print("Totally {} data received" .format(len(List_sub_message)))
    pub(client, MQTT_TOPIC_2, "data received", 1 )




client = mqtt.Client("subscriber_memory", clean_session=CLEAN_SESSION)
client.connect(MQTT_BROKER, PORT_ID, KEEP_ALIVE)
client.on_message = on_message


sub(client, MQTT_TOPIC_1, QOS_S)
time.sleep(2)

pub(client, MQTT_TOPIC_2, "message", QOS_P)
time.sleep(2)

client.loop_forever()



