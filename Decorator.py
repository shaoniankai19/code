# 装饰器的简单应用
# --------------------------------------------------------------
import hashlib
import random


def setpassword(word):
    md5 = hashlib.md5()
    md5.update(word.encode())
    return md5.hexdigest()


mima_list = random.choice(['12345', '123456', '1234'])
print(mima_list)
user = {'name': 'zk', 'mima': setpassword(mima_list)}

your_choice = input('请输入你的密码')


def is_login(fn):
    def inner(*args, **kwargs):
        if 'zk' and setpassword(your_choice) in user.values():
            return fn(*args, **kwargs)
        else:
            return print('密码错了')

    return inner


@is_login
def a():
    print('欢迎来到Chain Beijing')


a()
# -------------------------------------------------------------------
