"""
使用socket搭建一个简单的服务器
"""
import socket
sk = socket.socket()
sk.bind(('127.0.0.1',8080))#绑定端口
sk.listen()#监听

while True:
    conn, addr = sk.accept()
    data  = conn.recv(9000)
    print(data)
    conn.send(b'HTTP/1.1 200 ok\r\n\r\n ok')

