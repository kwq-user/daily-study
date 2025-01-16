# 此处用来展示bemfa.com相关推送主题对应案例
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(topic="test")


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


client = mqtt.Client(client_id="a86d04ad43f01ddc8fc30308bee4c2f4")
client.on_connect = on_connect
client.on_message = on_message

client.connect("bemfa.com",9501,60)

# 保持链接
client.loop_forever()

