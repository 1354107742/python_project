"""
使用socket搭建一个简单的服务器
"""
import socket
sk = socket.socket()
sk.bind(('127.0.0.1', 8080))  # 绑定端口
sk.listen()  # 监听


#定义路径函数
def abc(url):
    data = 'hello this is a func to client:{}'.format(url)
    return bytes(data ,encoding = 'utf-8')
def lalala(url):
    data = 'come on !:{}'.format(url)
    return bytes(data, encoding='utf-8')
#利用映射，优化掉之前的if判断
url_lis = [
    ('/abc/',abc),
    ('/lalala/',lalala)
]

#---------------建立连接，接受消息-----------------
while True:
    conn, addr = sk.accept()
    #接受消息
    data = conn.recv(9000)
    #---------------对消息进行处理----------------
    data_str = str(data, encoding='utf-8')
    #然后利用\r和\n进行切片
    #然后取出第一行的路径，得到请求行
    first_line = data_str.split('\r\n')[0]
    #取出url路径，得到目标文件路径
    url = first_line.split(' ')[1]
    #---------------业务逻辑处理部分-----------
    for i in url_lis:
         if i[0] == url:
            func = i[1]
            break
    else:
        func = None
    #利用python非0为Ture
    if func:
        msg = func(url)
    else:
        msg = b'404 not found!'
    #----------------响应部分-------------------
    conn.send(b'HTTP/1.1 200 ok\r\n\r\n')
    conn.send(msg)
    conn.close()
