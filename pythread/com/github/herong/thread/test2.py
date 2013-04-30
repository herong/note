# -*- coding:utf-8 -*-
# 功能：多线程数值累加
# author:herong
# date:2013/4/29
import threading
import time

#######类定义#################################
class MyThread(threading.Thread):
	'''求合线程类'''
	def __init__(self,name,start,end):
		threading.Thread.__init__(self,name=name)
		self.__end = end
		self.__start = start
	def run(self):
		global glTotal
		global gThreadCnt
		sum = 0
		for i in range(self.__start,self.__end+1):
			sum+=i
		time.sleep(1)
		#获取锁
		gLock.acquire()
		try:
			glTotal+=sum
			gThreadCnt+=1
		finally:
			#释放锁
			gLock.release()
			#pass;
		print '#Thread-%s,(sum(%s-%s))=%s\n'%(self.getName(),self.__start,self.__end,sum)
		#time.sleep(2)

#################全局变量区############################
#总和
glTotal = 0
#控制变量
gThreadCnt  = 0
#锁对象
gLock = threading.RLock()
goThreadArray = []

#################执行代码块############################
step = 10
for i in range(10,100+1,step):
	t = MyThread(i/10,i-step+1,i)
	goThreadArray.append(t)

for i in goThreadArray:
	i.start()
	#i.join()

#for i in goThreadArray:
	#i.join()
	
while gThreadCnt < 10:
	print 'wait...\n'
	time.sleep(1)

print 'Total:',glTotal
