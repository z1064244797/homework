# -*- coding:cp936 -*-

import urllib2,time,re
print "Start : %s" % time.ctime()
url = 'http://news.ncu.edu.cn/'

print'----------------��һ����������ҳ����----------------\n\n'
time.sleep(1)

count = 0 
a = 2
while (count < a):
    ncount = a - count 
    print'���ؽ���',ncount,'���ʼ'
    time.sleep(1)
    count += 1
print '\n\n----------------------���ؿ�ʼ----------------------\n\n' 
time.sleep(1)
r1 =True
while r1:
    try:
        response1 = urllib2.urlopen(url)
        code = response1.getcode()
        read = response1.read()
        print'״̬��Ϊ',code,'\n���سɹ�!'
        time.sleep(2)
        print'\nĿ����ҳ�Ѵ���read����'
        time.sleep(2)
        r1 = False
    except:
        print'����ʧ�ܣ��������缰������á�'
        r2 = True
        while r2:
            r = raw_input('�Ƿ�����? Y or n:\n')
            if r == 'Y':
                r2 = False
                r1 = True
            elif r == 'n':
                r2 = False
                r1 = False
                print'/n---------------------�����ѱ���ֹ----------------------'
                break
            else:
                print('����������������룡!')
                r2 = True

print'\n\n----------------�ڶ�������ȡ��ҳ����----------------\n\n'
time.sleep(1)

count = 0 
a = 2
while (count < a):
    ncount = a - count 
    print'���ؽ���',ncount,'���ʼ'
    time.sleep(1)
    count += 1
print '\n\n----------------------��ȡ��ʼ----------------------\n\n'
time.sleep(1)
p1 = r"(?<=<title>).+?(?=</title>)"
pattern1 = re.compile(p1)
matcher1 = re.search(pattern1,read)
print '������Ҫ����ȡ������:\n\n',matcher1.group(0)
time.sleep(3)
print '\n\n----------------------��ȡ���----------------------\n\n'
time.sleep(1)

count = 0 
a = 2
while (count < a):
    ncount = a - count 
    print'������',ncount,'���ر�'
    time.sleep(1)
    count += 1
print'\n\n---------------------�����ѱ���ֹ--------------------\n\nBy:������'
