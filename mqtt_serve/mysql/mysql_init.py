import pymysql

class MysqlLink:
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            port=3302,
            user='kwq_user',
            password='1250',
            db='bemfa.com-mqtt',
        )
        self.cursor = self.conn.cursor()

