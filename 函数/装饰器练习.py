# -*- coding: utf-8 -*-
# @Time    : 2018/11/19 18:35
# @Author  : ways
# @Email   : 1076377207@qq.com
# @File    : 装饰器练习.py
"""
一：编写函数，（函数执行的时间是随机的）
二：编写装饰器，为函数加上统计时间的功能
三：编写装饰器，为函数加上认证的功能
四：编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），要求登录成功一次，后续的函数都无需再输入用户名和密码
注意：从文件中读出字符串形式的字典，可以用eval('{"name":"egon","password":"123"}')转成字典格式
五：编写装饰器，为多个函数加上认证功能，要求登录成功一次，在超时时间内无需重复登录，超过了超时时间，则必须重新登录
六：编写下载网页内容的函数，要求功能是：用户传入一个url，函数返回下载页面的结果
七：为题目五编写装饰器，实现缓存网页内容的功能：
具体：实现下载的页面存放于文件中，如果文件内有值（文件大小不为0），就优先从文件中读取网页内容，否则，就去下载，然后存到文件中
扩展功能：用户可以选择缓存介质/缓存引擎，针对不同的url，缓存到不同的文件中
八：还记得我们用函数对象的概念，制作一个函数字典的操作吗，来来来，我们有更高大上的做法，在文件开头声明一个空字典，然后在每个函数前加上装饰器，完成自动添加到字典的操作
九 编写日志装饰器，实现功能如：一旦函数f1执行，则将消息2017-07-21 11:12:11 f1 run写入到日志文件中，日志文件路径可以指定
"""
import time

user_flag = False
login_time = 0
def login(func):
    def inner(*args, **kwargs):
        with open("user_password","r",encoding="utf-8") as f:
            user_data = f.readline().strip()
        user_data = eval(user_data)
        global user_flag
        global login_time
        if not user_flag:
            username = input("username:")
            password = input("password:")
            if username == user_data["name"] and password == user_data["password"]:
                login_time = time.time()
                func()
                user_flag = True
            else:
                print("fuck off...")
        elif time.time() - login_time > 2:
            username = input("username:")
            password = input("password:")
            if username == user_data["name"] and password == user_data["password"]:
                login_time = time.time()
                func()
                user_flag = True
        else:
            func()
    return inner

def wrapper(func):
    def inner(*args, **kwargs):
        time_start = time.time()
        func()
        time_stop = time.time()
        print(time_stop-time_start)
    return inner
@login
@wrapper
def spend_time1():
    time.sleep(2)
    print("函数一执行完毕")
@login
@wrapper
def spend_time2():
    time.sleep(2)
    print("函数二执行完毕")
@login
@wrapper
def spend_time3():
    time.sleep(1)
    print("函数三执行完毕")


spend_time1()
spend_time2()
spend_time3()

