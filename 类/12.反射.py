# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 20:21
# @Author  : ways
# @Email   : 1076377207@qq.com
# @File    : 12.反射.py
# 反射：通过字符串映射到对象的属性


class People:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self):
        print("学习中。。。")

p1 = People("ways", 12)

print(hasattr(p1,"name") )  #  p1.name  # p1.__dict__["name"]
print(hasattr(p1,"study") )  #  p1.name  # p1.__dict__["name"]

print(getattr(p1,"name",None))  # 如果不存在，则返回default 默认值

setattr(p1,"age",24)  # p1.age = 24

delattr(p1,"age")    # del obj.age
