import threading as thread
import paho.mqtt.client as mqtt

broker = "bemfa.com"
port = 9501


class Bemfa_Server:
    """
    Bemfa_Server用于链接bemfa.com的MQTT,一下是使用案例
            client_id = "a86d04ad43f01ddc8fc30308bee4c2f4"  -->个人账户ID
            Bemfa_Link = Bemfa_Server()                     -->首先实例化一个链接
            client = Bemfa_Link.client_init(client_id)      -->初始化链接，需要个人账户ID作为参数
            {
                # 创建线程-->在订阅状态下，为保持链接，需创建一个线程去保持链接
                myThread = thread.Thread(target=client.loop_forever)
                myThread.start()
            }
            Bemfa_Link.bemfa_sub(client, "test")            -->订阅主题
            Bemfa_Link.bemfa_pub(client, "test", "test")    -->给主题推送消息

    """
    def __init__(self):
        self.broker = broker
        self.port = port

    def on_connect(self, client, userdata, flags, rc, props):
        if rc == 0:
            print("成功链接bemfa.com")
        else:
            print("Fail %d\n", rc)

    def on_message(self, client, userdata, msg):
        """
        这个函数用来接受订阅数据
        可继承后自行DIY
        """
        print("获取内容:" + msg.payload.decode("utf-8"))

    def client_init(self, client_id):
        """
            这个函数用来初始化链接
            你只需要传入用户ID即可
        """
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id)
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.connect(broker, port, 60)
        return client

    def bemfa_sub(self, client, topic):
        """
            这个函数用来订阅一个主题
            回调函数on_message将打印接受到的数据
            你需要传入刚初始化好的链接client和你需要订阅的主题topic
        """
        client.subscribe(topic=topic)

    def bemfa_pub(self, client, topic, msg):
        """
            这个函数用来给指定主题推送消息
            需要传入参数:已初始化好的client链接,推送主题,推送内容
        """
        client.publish(topic=topic, payload=msg)

if __name__ == '__main__':
    client_id = "a86d04ad43f01ddc8fc30308bee4c2f4"
    Bemfa_Link = Bemfa_Server()
    client = Bemfa_Link.client_init(client_id)
    # 创建线程
    myThread = thread.Thread(target=client.loop_forever)
    myThread.start()
    Bemfa_Link.bemfa_sub(client, "test")
    Bemfa_Link.bemfa_pub(client, "test", "test")
