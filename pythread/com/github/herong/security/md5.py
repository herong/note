#-*- coding:gbk -*-'
'''
Created on 2013-5-8

@author: hr
'''
import hashlib

text = raw_input("请输入明文:")
m = hashlib.md5()
m.update(text)
ciphertext = m.hexdigest()

print "   明文:%s\n   密文:%s"%(text,ciphertext)

if __name__ == '__main__':
    pass