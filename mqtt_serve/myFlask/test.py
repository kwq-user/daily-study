import threading
import mqtt.Bemfa_Serve as Bemfa_Serve
import mysql.Mysql_Serve as Mysql_Serve


class Test(Bemfa_Serve.Bemfa_Serve):
    def __init__(self):
        super().__init__()
        self.mysql_server = Mysql_Serve.Mysql_Serve()

    def bemfa_sub(self, client, topic):
        super().bemfa_sub(client, topic)
        print(f"订阅{topic}中")
        self.mysql_server.mysql_create(topic)

    def on_message(self, client, userdata, msg):
        super().on_message(client, userdata, msg)
        self.mysql_server.mysql_add(msg.topic, msg.payload.decode("utf-8"))


if __name__ == '__main__':
    client_id = "a86d04ad43f01ddc8fc30308bee4c2f4"
    Link = Test()
    client = Link.client_init(client_id=client_id)
    # 创建线程
    myThread = threading.Thread(target=client.loop_forever)
    myThread.start()
    Link.bemfa_sub(client, 'num')
