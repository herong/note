#-*- coding:gbk -*-'
'''
核三框架本地化
由于原框架在获取md5值后，在转为十六进制的时候把高位为0的去掉了，所以在这里跟它保持一致
Created on 2013-5-8

@author: hr
'''
import hashlib
import os
import re
from string import Template
text = raw_input("请输入文件完整路径:")
pwd = raw_input("请输入默认密码:")
regex_pwd = "\\$pwd"

def getFile(filepath):
    if not os.path.isfile(filepath):
        print "不是文件：%s"%(filepath)
    f = None
    f2 = None
    try:     
        f = file(filepath,'r')
        rows = []
        for line in f.readlines():
            isMatch = re.search(regex_pwd,line)
            rline = line
            if isMatch is not None:
                sxh = geSxh()
                chipertext = getMd5dd(sxh,pwd)
                t = Template(line)
                rline = t.substitute(pwd=chipertext)
            rows.append(rline+"\n")
            
        f2 = file(filepath,'w')
        f2.writelines(rows)
        
    finally:
        if f is not None:
            f.close()
        if f2 is not None:
            f2.close()
    f2.flush()
    
    
def geSxh():
    pass

def getMd5dd(key,text):
    m = hashlib.md5()
    m.update(key+text)
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
    
    return especial_ciphertext

if __name__ == '__main__':
    pass