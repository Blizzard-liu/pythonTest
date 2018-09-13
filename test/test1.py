# encoding: utf-8
"""
@project = pythontest
@file = test1
@author = liu_bo
@create_time = 2018/9/6 11:16
"""
import time
import requests

print('   *', '  **', '  ***', '   |  ', sep='\n')


def text_create(name, msg):
    desktop_path = 'c:/Users/admin/Desktop/python/'
    full_path = desktop_path + name + '.txt'
    file = open(full_path, 'w')
    file.write(msg)
    file.close()
    print('done')


def text_filter(word, censored_word='lame', changed_word="Awesome"):
    return word.replace(censored_word, changed_word)


def censored_text_create(name, msg):
    msg = text_filter(msg)
    text_create(name, msg)


censored_text_create('try', 'lame,lame')


# text_create('haha', 'hello world')


def account_login():
    password = input('PassWord:')
    password_correct = password == '123'
    if password_correct:
        print('Login success!')
    else:
        print('Wrong password')
        account_login()


# account_login()


for num in range(1, 11):
    print(str(num) + ' +1 =', num + 1)

for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = %02d ' % (i, j, i * j))
        # print('{} * {} = {}'.format(i, j, i * j))

for a, b in zip([1, 2, 3], ['a', 'b']):
    print(a, 'is', b)

t0 = time.perf_counter()
b = [i for i in range(1, 20000)]
print(time.perf_counter() - t0, 'seconds process time ')

a = [i ** 2 for i in range(1, 10)]
print(a)
for a1, num1 in enumerate(a):
    print(a1, ' is ', num1)

k = [n for n in range(1, 10) if n % 2 == 0]
k.append('aaaa')
print(k)

d = {i: i + 1 for i in range(4)}
print(d)

g = {i: j.upper() for i, j in zip(range(1, 6), 'abcde')}
print(g)

l = [m + n for m in 'ABC' for n in '123']
print(l)

print(list(map(lambda x: x * x, (1, 2, 3))))

r = requests.get("https://www.shiguangkey.com/course/list?cateId=282")
print(r)
