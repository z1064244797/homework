# -*- coding:cp936 -*-

import urllib2,time,re
print "Start : %s" % time.ctime()
url = 'http://news.ncu.edu.cn/'

print'----------------第一步，加载网页内容----------------\n\n'
time.sleep(1)

count = 0 
a = 2
while (count < a):
    ncount = a - count 
    print'加载将于',ncount,'秒后开始'
    time.sleep(1)
    count += 1
print '\n\n----------------------加载开始----------------------\n\n' 
time.sleep(1)
r1 =True
while r1:
    try:
        response1 = urllib2.urlopen(url)
        code = response1.getcode()
        read = response1.read()
        print'状态码为',code,'\n加载成功!'
        time.sleep(2)
        print'\n目标网页已存入read变量'
        time.sleep(2)
        r1 = False
    except:
        print'加载失败，请检查网络及相关设置。'
        r2 = True
        while r2:
            r = raw_input('是否重试? Y or n:\n')
            if r == 'Y':
                r2 = False
                r1 = True
            elif r == 'n':
                r2 = False
                r1 = False
                print'/n---------------------程序已被终止----------------------'
                break
            else:
                print('输入错误，请重新输入！!')
                r2 = True

print'\n\n----------------第二步，爬取网页标题----------------\n\n'
time.sleep(1)

count = 0 
a = 2
while (count < a):
    ncount = a - count 
    print'加载将于',ncount,'秒后开始'
    time.sleep(1)
    count += 1
print '\n\n----------------------爬取开始----------------------\n\n'
time.sleep(1)
p1 = r"(?<=<title>).+?(?=</title>)"
pattern1 = re.compile(p1)
matcher1 = re.search(pattern1,read)
print '以下是要求爬取的内容:\n\n',matcher1.group(0)
time.sleep(3)
print '\n\n----------------------爬取完毕----------------------\n\n'
time.sleep(1)

count = 0 
a = 2
while (count < a):
    ncount = a - count 
    print'程序将于',ncount,'秒后关闭'
    time.sleep(1)
    count += 1
print'\n\n---------------------程序已被终止--------------------\n\nBy:张义主'
