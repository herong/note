# -*- coding:utf-8 -*-
# author:herong
# date:2013/4/29
import threading
import time
class mythread(threading.Thread):
    def __init__(self,num):
            threading.Thread.__init__(self)
            self.num = num
    def run(self):
            global x
            lock.acquire()
            try:
                x+=1
                time.sleep(2)
                print '#Thread-',self.num,'+',1,'=',x
            finally:
                lock.release()
            
lock = threading.RLock()
t1 = []
for i in range(10):
    t = mythread(str(i))
    t1.append(t)

x = 0
for i in t1:
    i.start()

    
