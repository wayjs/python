# -*- coding: utf-8 -*-
# @Time    : 2018/11/19 14:00
# @Author  : ways
# @Email   : 1076377207@qq.com
# @File    : 名称空间问题.py
x = 1


def f1():
    def f2():
        print(x)
    return f2


x = 100


def f3(func):
    x = 2
    func()


x = 10000
f3(f1())
