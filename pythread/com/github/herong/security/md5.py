#-*- coding:gbk -*-'
'''
Created on 2013-5-8

@author: hr
'''
import hashlib

text = raw_input("����������:")
m = hashlib.md5()
m.update(text)
ciphertext = m.hexdigest()

print "   ����:%s\n   ����:%s"%(text,ciphertext)

if __name__ == '__main__':
    pass