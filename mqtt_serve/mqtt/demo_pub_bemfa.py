# 此处用来展示bemfa.com相关推送主题对应案例
import time
import paho.mqtt.client as mqtt

import _thread as thread


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.publish(topic="test", payload="123")


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


client = mqtt.Client(client_id="a86d04ad43f01ddc8fc30308bee4c2f4")
client.on_connect = on_connect
client.on_message = on_message
client.connect("bemfa.com",9501,60)

thread.start_new_thread(client.loop_forever,())

count = 0;
while True:
    time.sleep(5)
    count += 1
    print(count)
    client.publish(topic="test", payload=count)