import pymysql

# データベースへの接続を定義するためのクラス
class DB:
    def getConnection():
        try:
            conn = pymysql.connect(
                host="localhost",
                user="user",
                password="testuser",
                database="chatapp",
                charset="utf8",
                cursorclass=pymysql.cursors.DictCursor
                )
            return conn
        except (ConnectionError):
            print("コネクションエラーです")
            conn.close()