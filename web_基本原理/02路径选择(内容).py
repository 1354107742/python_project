"""
使用socket搭建一个简单的服务器
"""
import socket
sk = socket.socket()
sk.bind(('127.0.0.1', 8080))  # 绑定端口
sk.listen()  # 监听

while True:
    conn, addr = sk.accept()
    data = conn.recv(9000)
    data_str = str(data,encoding = 'utf-8')
    print(data)
    #然后利用\r和\n进行切片
    #然后取出第一行的路径
    first_line = data_str.split('\r\n')[0]
    #取出url路径
    url = first_line.split(' ')[1]
    print(url)
    if url == '/abc':
        msg = b'hands up!'
    elif url == '/lalala':
        msg = b'come on !'
    else:
        msg = b'404 not found'
    conn.send(b'HTTP/1.1 200 ok\r\n\r\n')
    conn.send(msg)
    conn.close()


