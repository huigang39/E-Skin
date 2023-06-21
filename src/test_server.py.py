import joblib
import pandas as pd
import socket

def start_server(label_map, model):
    ip_address = '10.67.104.154'

    host = ip_address
    port = 12345

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(1)


    while True:
        print("开始服务，等待连接...")
        conn, addr = server_socket.accept()
        print(f"连接来自：{str(addr)}")
        data = conn.recv(1024).decode()
        if data:  # Only process data if it's not empty
            print(f"来自连接用户：{str(data)}")

            data = data.strip()

            # 将字符串转换为列表
            lst = data.split(",")

            # 将字符串转换为float类型
            lst = list(map(float, lst))

            # 将值传递给DataFrame函数
            new_data = pd.DataFrame(lst).T

            y_pred = model.predict(new_data)[0]
            y_pred = label_map[y_pred]
            conn.send(y_pred.encode())

if __name__ == '__main__':
    label_map = {0: '食指', 1: '小指', 2: '中指',3: '休息', 4: '无名指', 5: '大拇指', 6: '胜利手势'}

    model = joblib.load('model/model.pkl')

    start_server(label_map, model)
