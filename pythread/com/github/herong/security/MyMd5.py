#-*- coding:gbk -*-'
'''
������ܱ��ػ�
����ԭ����ڻ�ȡmd5ֵ����תΪʮ�����Ƶ�ʱ��Ѹ�λΪ0��ȥ���ˣ������������������һ��
Created on 2013-5-8

@author: hr
'''
import hashlib

text = raw_input("����������:")
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

print "   ����:%s\n   ����:%s\n������:%s"%(text,ciphertext,especial_ciphertext)

if __name__ == '__main__':
    pass