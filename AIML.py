#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('hello world')
print('wt ur name?')
myname = input()
print('it is good to meet u,'+ myname)
print('the length of ur name is:')
print(len(myname))
print('what is ur age?')
myage = input()
print('you will be' + str(int(myage) +1)+ 'in a year.')


# In[ ]:





# In[28]:


import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'it is certain'
    elif answerNumber == 2:
        return 'it is decidedly so'
    elif answerNumber == 3:
        return 'yes'
    elif answerNumber == 4 :
        return 'replay hazy try agin'
    elif answerNumber == 5:
        return 'ask agin later'
    elif answerNumber == 6:
        return 'concentrate and ask again'
    elif answerNumber == 7:
        return 'my replay is no'
    elif answerNumber == 8:
        return 'outlook not so good'
    elif answerNumber == 9:
        return 'very doubtful'
r =  random.randint(1,9)
fortune = getAnswer(r)
print(fortune)
        


# In[ ]:





# In[7]:


print('hello world')


# In[8]:


str(0)


# In[15]:


str(-3.14)


# In[10]:


int('42')


# In[11]:


int(1.99)


# In[12]:


float('3.14')


# In[13]:


float(10)


# In[17]:


spam = input()


# In[18]:


spam


# In[24]:


print('you will be'  + str(int(myage) + 1) +  'in a year.')


# In[25]:


print('you will be'  + str(int('4') + 1) +  'in a year.')


# In[26]:


print('you will be'  + str(int(4+1) + 1) +  'in a year.')


# In[27]:


print('you will be'  + str(int(5) + 1) +  'in a year.')


# In[28]:


print('you will be'  + str(int('5') + 1) +  'in a year.')


# In[31]:


print('you will be 5'    +  'in a year.')


# In[32]:


spam = True


# In[33]:


spam


# In[34]:


True = 2+2


# In[ ]:


while True:
    print('who are u?')
    name = input()
    if name != 'joe':
        continue
    print('hello, joe. what is the password?(it is a fish.)')
    password = input()
    if password == 'swordfish':
          break
print('access granted')


# In[1]:


print('my name')
for i in range(s):
    print('jimmy five times ('+str (i) +')')


# In[7]:


for i in range(12,16):
    print(1)


# In[4]:


for i in range(0,10,2):
    print(i)


# In[6]:


for i in range(5,-1,-1):
    print(i)


# In[9]:


import random
for i in range(5):
    print(random.randint(1,10))


# In[11]:


import sys
while True:
    print('type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
        print('you typed' + response +'.')


# In[13]:


def hello():
    print('howdey!')
    print('howdey!!')
    print('hello thrre')
    


# In[14]:


hello()


# In[19]:


def hello(name):
    print('hello '+name)


# In[20]:


hello('alice')


# In[21]:


hello('bob')


# In[32]:


print('cats','dogs','mice',sep = ',')


# In[33]:


print('cats','dogs','mice')


# In[34]:


def spam():
    eggs = 99
    becon()
    print(eggs)
def becon():
    ham = 101
    egg = 0
spam()


# In[36]:


def spam():
    print(egg)
egg =42
spam()
print(egg)


# In[40]:


def spam(divby):
    return 42 /divby


# In[41]:


spam(2)


# In[42]:


spam(0)


# In[48]:


def spam(divideby):
    try:
        return 42/divideby
    except zerodividebyerror:
        print('error: invalid argument')


# In[50]:


spam(2)


# In[5]:


import random
scretNumber = random.randint(1,20)
print('i am thinking of a number between 1 to 10')
for guessesTaken in range(1,7):
    print('take a guess')
    guesses = int(input())
    if guess <secretNumber:
        print('ypur guess is too low')
    elif guess > secretNumber:
            print('your guess is too high')
    else:
            break
if guess == secretNumber:
        print('good')
else:
     print('nope')


# In[3]:


spam = ['cat','rat','bat']


# In[4]:


spam[-2]


# In[2]:


m1=int(input("enter marks for test:"))
m2=int(input("enter marks for test2"))
m3 = int(input("enter marks for test3"))

if m1<= m2 and m1<=m3:
    avgmarks = (m2+m3)/2
elif m2<=m1 and m2<= m3:
        avgmarks = (m1+m2)/2
elif m3<=m1 and m2<+m2:
      avgmarks = (m1+m2)/2
print("average of best two test marks out of three test's marks is",avgmarks)


# In[ ]:


val = int(input('enter a value :')
        


# insert sort:

# In[1]:


import random 
def merge_sort(1st):
    if len(1st)>1:
        mid = len


# In[ ]:




