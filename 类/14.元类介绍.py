# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 22:53
# @Author  : ways
# @Email   : 1076377207@qq.com
# @File    : 14.元类介绍.py
"""
知识储备 exec python 代码放到字符串中执行
#参数1：字符串形式的命令
#参数2：全局作用域(字典形式)，如果不指定，就默认使用globals()
#参数3：局部作用域（字典形式），如果不指定，就默认使用locals()
"""
# g = {
#     "x":1,
#     "y":2
# }
# l = {}
# exec("""
# global x,m
# x = 10
# m = 100
# z = 3
# """,g,l)
# print(g)
# print(l)
"""
#  一切皆为对象，对象都可以怎么用？
#1、都可以被引用，x =obj
#2、都可以当作函数的参数传入
#3、都可当作函数的返回值
#4、都可以当作容器类的元素，l = [func,time,obj,1]
"""

#类也是对象，Foo= type(....)
# class Foo:
#     pass
#
#
# obj = Foo()
# print(type(obj))
# print(type(Foo))
# 产生类的类就称之为元类，默认所有用class定义的类，他们的元类是type


# 定义类的两种方式：
#     方式一:class
#     class People:    # People = type(.....)
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def eat(self):
#         pass
#     方式二:type
#     定义类的三要素：类名，类的基类们，类的名称空间
class_name = "People"
class_bases =( object,)
class_body="""
def __init__(self, name, age):
    self.name = name
    self.age = age
def eat(self):
    print("is eating")
 """
class_dict = {}
exec(class_body, globals(), class_dict)
People = type(class_name,class_bases,class_dict)
obj = People("egon",18)
obj.eat()


