# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 22:55
# @Author  : ways
# @Email   : 1076377207@qq.com
# @File    : 19.绑定方法与非绑定方法.py
"""
在类内部定义的函数，分为两大类：
    一、绑定方法：绑定给谁，就由谁调用，谁来调用，就会把调用者当作第一个参数自动传入。
        绑定到对象的方法：在类内定义的没有被任何装饰器修饰的
        绑定到类的方法: 在类内部定义的，被装饰器classmethod修饰的
    二、非绑定方法：没有自动传值这么一说,就是类中一个普通工具而已，谁都可以调用
        非绑定方法：不与类或者对象绑定

"""


class Foo:

    def __init__(self, name):
        self.name = name

    def tell(self):
        print("名字是:%s" % self.name)

    @classmethod
    def func(cls):    # <class '__main__.Foo'>
         print(cls)

    @staticmethod
    def func1(x, y):
        print(x, y)


f = Foo("egon")
print(Foo.tell)     # <function Foo.tell at 0x0000023531CAEC80>  调用需要采用  Foo.tell(f)，就像普通函数一样
print(f.tell)    # <bound method Foo.tell of <__main__.Foo object at 0x000002352AC68080>>
print(Foo.func)    # <bound method Foo.func of <class '__main__.Foo'>>
Foo.func()
print(Foo)    # <class '__main__.Foo'>
print(Foo.func1)    # <function Foo.func1 at 0x00000247C975EE18>
print(f.func1)    # <function Foo.func1 at 0x00000247C975EE18>
