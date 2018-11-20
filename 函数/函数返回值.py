# -*- coding: utf-8 -*-
# @Time    : 2018/11/19 10:11
# @Author  : ways
# @Email   : 1076377207@qq.com
# @File    : 函数返回值.py


def func():
    return 1,[2,3,4],{"name":"ways","age":13}


def func2():
    return 1


x = func()
y = func2()
print(x,type(x))
print(y,type(y))


c = lambda x,y:x*y
print(c(2,5))