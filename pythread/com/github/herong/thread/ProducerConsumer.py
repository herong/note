# -*- coding:gbk -*-
'''
Created on 2013-4-30

@author: herong
模拟多生产者和多消费者
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
                self.__taskQueue.put(Task("任务-"+str(taskId),"None"))
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
        print "【生产者】产生任务:%s,任务类型:%s"%(self.__name,self.__type)
        
    def run(self):
        print "【消费者】执行行务%s ......"%(self.__name)
        time.sleep(1)
        print "【消费者】任务%s执行完毕!"%(self.__name)

if __name__ == '__main__':
    gTaskQueue = Queue.Queue(1)
    gProducerNum = 10
    gConsumerNum = 1
    gTaskNum = 2
    gTaskTotal = 0
    gMaxTaskTotal = 10
    gLock = threading.RLock()
    for i in range(gConsumerNum):
        Consumer("消费者"+str(i+1)+"#", gTaskQueue, gTaskNum).start()
    for i in range(gProducerNum):
        Producer("生产者"+str(i+1)+"#", gTaskQueue, gTaskNum).start()
