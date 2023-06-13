import socket
import pickle

model = pickle.load(open('model/model.pkl', 'rb'))

host = 'localhost'
port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

model_bytes = pickle.dumps(model)

try:
    s.sendall(model_bytes)
    s.shutdown(socket.SHUT_WR)
    data_bytes = b''
    while True:
        chunk = s.recv(1024)
        if not chunk:
            break
        data_bytes += chunk
    data = pickle.loads(data_bytes)
    print(data)
except ConnectionResetError:
    print("连接意外关闭")
finally:
    s.close()