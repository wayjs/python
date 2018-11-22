# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 20:50
# @Author  : ways
# @Email   : 1076377207@qq.com
# @File    : 13.内置方法.py
# isinstance和issubclass

class People:

    def __init__(self):
        pass

class Student(People):
    pass

stu = Student()
print(isinstance(stu,Student))
print(issubclass(Student,People))

# item 系列

# class Foo:
#     def __init__(self,name):
#         self.name = name
#
#     def __getitem__(self, item):
#         # print("getitem")
#         # print(item)
#         return self.__dict__.get(item)
#
#     def __setitem__(self, key, value):
#         # print("setitem")
#         # print(key,value)
#         self.__dict__[key] = value
#     def __delitem__(self, key):
#         # print("delitem")
#         # print(key)
#         self.__dict__.pop(key)
# obj = Foo("ways")
# # obj.属性名
# obj['name']    # 触发__getitem__函数 完成obj.name取值
# #obj.name = "ddd"
# obj["sex"] = "male"    # 触发__setietm__函数
#
# # del obj.name  删除属性
#
# del obj["name"]
# print(obj.__dict__)


#  __str__: print()的时候触发，
# 会在某种情况下自动触发，实现类的定制
# class People:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         # print("======>")
#         return "<name:%s,age:%s>" %(self.name,self.age)
# obj = People("ways", 24)
# print(obj)    #obj.__str__()


# __del__

class Teacher:
    def __del__(self):
        pass
t = Teacher()
del t