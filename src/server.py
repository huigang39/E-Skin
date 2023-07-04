import joblib
import pandas as pd
import socket
import serial
import time
from processData import extract_features

def start_server(label_map, model):
    host = socket.gethostname()
    port = 2333

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(1)

    batch_size = 100  # 缓冲区大小
    buffer = []

    while True:
        print("开始服务，等待连接...")
        conn, addr = server_socket.accept()
        print(f"连接来自：{str(addr)}")

        # 从串口读取原始数据并提取特征值
        ser = serial.Serial('/dev/ttyS0', 9600)
        start_time = time.time()
        while True:
            line = ser.readline().decode().strip()
            if line:
                buffer.append(float(line))
                if len(buffer) >= batch_size or time.time() - start_time > 1:
                    new_data = extract_features(buffer)
                    y_pred = model.predict(new_data)[0]
                    y_pred = label_map[y_pred]
                    conn.send(y_pred.encode())
                    buffer = []
                    start_time = time.time()
        ser.close()

if __name__ == '__main__':
    label_map = {0: '食指', 1: '小指', 2: '中指', 3: '休息', 4: '无名指', 5: '大拇指', 6: '胜利手势'}

    model = joblib.load('model/model.pkl')

    start_server(label_map, model)
