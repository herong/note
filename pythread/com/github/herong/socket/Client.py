#-*- coding:gbk -*-
'''
Created on 2013-4-30

@author: herong
'''
import threading
import sys
from socket import *

class Client(threading.Thread):
    '''客户端类'''
    __port = None
    __socket = None
    __host = None
    __active = True
    def __init__(self,host,port=8001):
        threading.Thread.__init__(self)
        self.__port = port
        self.__host = host
        self.__socket = socket(AF_INET,SOCK_STREAM)
        self.__socket.connect((self.__host,self.__port))
        print "成功连接服务端%s,端口:%s"%(self.__host,self.__port)
        
    def run(self):
        try:
            while self.__active:
                cmd = raw_input("请输入请求服务端指令:")
                self.__socket.send(cmd)
                
                while 1:
                    recvData = self.__socket.recv(gBufferSize)
                    print "服务端返回信息：%s"%(recvData)
                    if cmd == "exit":
                        sys.exit(0)
                    if '[end]'   in recvData:
                        break
        finally:
            self.__socket.close()
           
            
gBufferSize = 1024
            
if __name__ == '__main__':
    Client("127.0.0.1",8001).start()