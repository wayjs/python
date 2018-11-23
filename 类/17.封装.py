# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 13:43
# @Author  : ways
# @Email   : 1076377207@qq.com
# @File    : 17.封装.py


# class A:
#     __x = 1    # _A__x = 1
#
#     def __init__(self, name):
#         self.__name = name    # self._A__name = name
#
#     def __foo(self):    # _A__foo
#         print("run foo")
#
#
# print(A.__dict__)
"""
这中变形的特点：
    1、在类外部无法直接访问
    2、在类内部可以直接访问，因为在类定义阶段，已经变形了
    3、子类无法覆盖父类__开头的属性
"""


# class Foo:
#     def __func(self):    # 不会重写，类名就不一样 _Foo_func
#         print("from foo")
#
#
# class Bar(Foo):
#     def __func(self):    # _Bar__func
#         print("from bar")
#
# b = Bar()
# b.func()
"""
总结这种变形需要注意的问题：
    1、这种机制，并没有真正意义上限制我们从外部直接访问属性，知道了类名和属性名就可以拼写出名字：_类名__属性,然后就可以直接访问了，如a_A__N
    2、变形的过程只在类的定义是发生一次，在定义后的赋值操作，不会变形
        a = A()
        a.__y=1
    3、在继承中，父类如果不想让子类覆盖自己的方法，可以将方法为私有的
"""
# 验证问题3：
# class Foo:
#
#     def __foo(self):
#         print("from foo")
#     def bar(self):
#         self.__foo()
# class Bar(Foo):
#     def __foo(self):
#         print("from Bar")
# bar = Bar()
# bar.bar()

