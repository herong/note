#-*- coding:gbk -*-
'''
Created on 2013-4-30

@author: herong
'''
import threading
from socket import *
import time
class process(threading.Thread):
    '''处理类'''
    __client = None
    __addr = None
    def __init__(self,client,addr):
        threading.Thread.__init__(self)
        self.__client = client
        self.__addr = addr
        print "客户端%s连接成功!"%(self.__addr[0])
    def run(self ):
        try:
            while True:
                recvData = self.__client.recv(gBufferSize)
                self.__client.send("客户端%s请求[%s]处理.......\n"%(self.__addr[0],recvData))
                print '处理中......'
                time.sleep(1)
                print '处理完毕.'
                self.__client.send("客户端%s请求[%s]处理完毕!\n"%(self.__addr[0],recvData))
                self.__client.send("[end]\n")
                
                if recvData == "exit":
                    self.__client.send("服务器退出!\n")
                    break
        finally:
            self.__client.close()
            
class Server(threading.Thread):
    '''服务端类'''
    __port = None
    __socket = None
    __active = True
    def __init__(self,port=8001,backlog=10):
        threading.Thread.__init__(self)
        self.__port = port
        self.__socket = socket(AF_INET,SOCK_STREAM)
        self.__socket.bind(("",self.__port))
        self.__socket.listen(backlog)
        print "服务开启，开始接收客户端请求..."
    def run(self):
        try:
            while self.__active:
                client ,addr = self.__socket.accept()
                print "client:%s,addr:%s"%(client,addr)
                p = process(client ,addr)
                p.setDaemon(True)
                p.start()
        finally:
            self.__socket.close()
            
gBufferSize = 1024
            
if __name__ == '__main__':
    Server(8001,5).start()