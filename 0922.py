#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('python --version')


# In[2]:


get_ipython().system('pwd')


# In[3]:


get_ipython().system('ls')


# In[4]:


get_ipython().system('ls -al')


# In[ ]:





# In[5]:


get_ipython().system('cat test.dat')


# In[6]:


get_ipython().system('cat data.dat')


# In[20]:


fread = None
try :
    fread = open('data.dat', 'r')

    for line in fread.readlines():      #readlines (가장 쉬운 방법)
        print(line, end='')
except :
    print('File Not Found')
finally :
    fread.close()


# In[23]:


poet = """                 
죽는 날까지 하늘을 우르러
한점 부끄럼이 없기를、
잎새에 이는 바람에도
나는 괴로워했다。
별을 노래하는 마음으로
모든 죽어가는것을 사랑해야지
그리고 나한테 주어진 길을
거러가야겠다。

오늘밤에도 별이 바람에 스치운다.
"""


# In[24]:


fwrite = None
try:
    fwrite = open('서시.txt', 'w')
    fwrite.write(poet)
    print("File Save Successfully.")
except Exception as err:                #디스크 용량이 없거나 할 때 오류 발생
    print(err)
finally:
    fwrite.close()


# In[26]:


with open('서시.txt', 'rt') as fread :
    try:
        count = 1
        for line in fread.readlines() :     #readlines는 리스트를 return함
            print(f'{count} : {line}', end='')
            count += 1
    except :
        print('File Not Found')


# In[27]:


import json


# In[29]:


list_ = ['Hello, World', 5, True, 89.5]
type(list_)


# In[30]:


str_ = json.dumps(list_)
type(str_)


# In[31]:


print(str_)


# In[42]:


obj = json.loads(str_)
type(obj)


# In[43]:


obj[2]


# In[54]:


student = {
    "hakbun" : "2023-003",
    "name" : "한지민",
    "age" : 24,
    "address" : "서울시 강남구 역삼동" 
}
type(student)


# In[55]:


str_ = json.dumps(student)
type(str_)


# In[56]:


with open('student.dat', 'wt') as fwrite :
    fwrite.write(str_)
    print("File Save Successfully.")


# In[59]:


with open('student.dat', 'rt') as fread :
    result = fread.read()
    #print(type(result))
    obj = json.loads(result)
    #print(type(obj))
    print(f"name = {obj['name']}, age = {obj['age']}")


# In[63]:


with open('sungjuk.json', 'rt') as fread :
    result = json.load(fread)    #load = read() -> loads()
    #print(type(result))         #list
    #print(len(result))
    #print(type(result[0]))      #dict
    print(result[0]['irum'])


# In[64]:


import os
print(os.name)


# In[65]:


print(os.getcwd())


# In[66]:


os.chdir('/')
print(os.getcwd())


# In[67]:


import sys


# In[68]:


print(f"Version : {sys.version}")
print(f"Version Info : {sys.version_info}")
print(f"Platform : {sys.platform}")


# In[69]:


import platform


# In[71]:


print(f"Platform Architecture : {platform.uname()}")


# In[72]:


import socket


# In[74]:


print(f"Host name : {socket.gethostname()}")


# In[75]:


hostname = socket.gethostbyname()
print(socket.gethostbyname(hostname))


# In[76]:


print(socket.gethostbyname('www.google.com'))


# In[78]:


print(os.system("ls"))


# In[79]:


os.system("cd ~")


# In[80]:


print(os.system("ls"))


# In[81]:


os.chdir("/home/ubuntu")


# In[82]:


print(os.system('ls'))


# In[83]:


import subprocess


# In[86]:


subprocess.run["ls", "-a"])


# In[87]:


get_ipython().system('pip list')


# In[88]:


get_ipython().system('pip install pymysql')


# In[ ]:




