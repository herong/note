#-*- coding:gbk -*-'
'''
核三框架本地化
由于原框架在获取md5值后，在转为十六进制的时候把高位为0的去掉了，所以在这里跟它保持一致
Created on 2013-5-8

@author: hr
'''
import hashlib

text = raw_input("请输入明文:")
m = hashlib.md5()
m.update(text)
ciphertext = m.hexdigest()
especial_ciphertext = ""
n=0
for i in range(16):
    n =i * 2
    k = ciphertext[n]
    if  k != "0":
        especial_ciphertext = especial_ciphertext + ciphertext[n] + ciphertext[n+1]
    else:
        especial_ciphertext = especial_ciphertext +  ciphertext[n+1]

print "   明文:%s\n   密文:%s\n特密文:%s"%(text,ciphertext,especial_ciphertext)

if __name__ == '__main__':
    pass