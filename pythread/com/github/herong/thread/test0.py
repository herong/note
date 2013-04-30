# -*- coding:utf-8 -*-
# 功能：多线程数值累加
# author:herong
# date:2013/4/29
import thread

def run(num):
	for i in range(num):
		print i

		
thread.start_new_thread(run,(10,))
