#-*- coding:gbk -*-'
'''
������ܱ��ػ�
����ԭ����ڻ�ȡmd5ֵ����תΪʮ�����Ƶ�ʱ��Ѹ�λΪ0��ȥ���ˣ������������������һ��
Created on 2013-5-8

@author: hr
'''
import hashlib
import os
import re
from string import Template
text = raw_input("�������ļ�����·��:")
pwd = raw_input("������Ĭ������:")
regex_pwd = "\\$pwd"

def getFile(filepath):
    if not os.path.isfile(filepath):
        print "�����ļ���%s"%(filepath)
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