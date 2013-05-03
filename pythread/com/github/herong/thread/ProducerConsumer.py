# -*- coding:gbk -*-
'''
Created on 2013-4-30

@author: herong
ģ��������ߺͶ�������
'''
import threading
import Queue
import time


class Producer(threading.Thread):
    __taskQueue = Queue.Empty
    __taskNum = 1
    def __init__(self,name,taskQueue,taskNum=1):
        threading.Thread.__init__(self, name=name)
        self.__taskQueue = taskQueue
    def run(self):
        global gTaskTotal,gMaxTaskTotal
        taskId = 0
        while(True):
            #for i in range(self.__taskNum):
                try:
                    gLock.acquire()
                    gTaskTotal +=1
                    taskId = gTaskTotal
                    if taskId >gMaxTaskTotal:
                        break
                finally:
                    gLock.release()
                self.__taskQueue.put(Task("����-"+str(taskId),"None"))
                time.sleep(2)

        
class Consumer(threading.Thread):
    __taskQueue = Queue.Empty
    __taskNum = 1
    def __init__(self,name,taskQueue,taskNum=1):
        threading.Thread.__init__(self, name=name)
        self.__taskQueue = taskQueue
        self.__taskNum = taskNum
    def run(self):

        while(True):
            #for i in range(self.__taskNum):
                task = self.__taskQueue.get()
                task.start()
               
            
        
class Task(threading.Thread):
    __name = None
    __type = None
    def __init__(self,name,type):
        threading.Thread.__init__(self, name=name)
        self.__name = name
        self.__type = type
        print "�������ߡ���������:%s,��������:%s"%(self.__name,self.__type)
        
    def run(self):
        print "�������ߡ�ִ������%s ......"%(self.__name)
        time.sleep(1)
        print "�������ߡ�����%sִ�����!"%(self.__name)

if __name__ == '__main__':
    gTaskQueue = Queue.Queue(1)
    gProducerNum = 10
    gConsumerNum = 1
    gTaskNum = 2
    gTaskTotal = 0
    gMaxTaskTotal = 10
    gLock = threading.RLock()
    for i in range(gConsumerNum):
        Consumer("������"+str(i+1)+"#", gTaskQueue, gTaskNum).start()
    for i in range(gProducerNum):
        Producer("������"+str(i+1)+"#", gTaskQueue, gTaskNum).start()
