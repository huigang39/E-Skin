import joblib
import pandas as pd
import socket


def start_server(label_map, model):
    host = socket.gethostname()
    port = 2333

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(1)

    while True:
        print("开始服务，等待连接...")
        conn, addr = server_socket.accept()
        print(f"连接来自：{str(addr)}")

        data = '0.029437,0.051465,0.089432,0.016893,0.014127,0.017735,0.019645,0.014079,0.030692,0.052209,0.08977,0.019609,0.016973,0.020182,0.021575,0.017081,-0.16406,-0.28906,-0.53906,-0.054688,-0.054688,-0.11719,-0.125,-0.054688,0.09375,0.16406,0.3125,0.03125,0.039063,0.046875,0.0625,0.03125,53,49,56,39,21,27,31,23,0.074323,0.11297,0.21297,0.050417,0.039271,0.047031,0.05099,0.036354,0.03125,0.054688,0.03125,0.039063,0.03125,0.046875,0.023438,0.023438,0.017896,0.02666,0.04566,0.013029,0.010639,0.011585,0.011896,0.010152,4.3672,6.6563,11.773,2.9219,2.3594,2.6797,2.8047,2.3516,2,3,6,0,0,1,1,0'

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
    label_map = {0: '食指', 1: '小指', 2: '中指',
                 3: '休息', 4: '无名指', 5: '大拇指', 6: '胜利手势'}

    model = joblib.load('model/model.pkl')

    start_server(label_map, model)
