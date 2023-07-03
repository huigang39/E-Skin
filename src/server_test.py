import socket
import sys
import pickle
import pandas as pd

# 创建 socket 对象
serversocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
# host = socket.gethostname()

# 获取当前IP地址
host = '10.67.94.167'

port = 2333

# 绑定端口号
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)

while True:
    # 建立客户端连接
    clientsocket,addr = serversocket.accept()

    print("连接地址: %s" % str(addr))

    model = pickle.load(open('model/model.pkl', 'rb'))

    new_data = pd.DataFrame([[0.047508,0.074164,0.086584,0.038356,0.023736,0.018826,0.034587,0.064517,0.048584,0.074464,0.086861,0.039348,0.025848,0.021021,0.035835,0.06493,-0.17188,-0.19531,-0.28906,-0.13281,-0.078125,-0.054688,-0.14063,-0.20313,0.09375,0.27344,0.22656,0.09375,0.039063,0.039063,0.070313,0.1875,73,82,72,68,55,41,74,85,0.13984,0.22589,0.26599,0.1149,0.068229,0.058385,0.099792,0.19818,0.13281,0.22656,0.16406,0.10156,0.085938,0.054688,0.054688,0.27344,0.038322,0.055861,0.065431,0.029649,0.018993,0.014701,0.027838,0.050236,8.6641,13.484,15.406,6.9375,4.1484,3.3984,6.1328,12.617,4,3,5,1,0,0,0,3]])

    y_pred = model.predict(new_data)[0]

    clientsocket.send(y_pred)
    clientsocket.close()
