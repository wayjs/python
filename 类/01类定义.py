# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 9:10
# @Author  : ways
# @Email   : 1076377207@qq.com
# @File    : 01类定义.py
#先定义类(抽象的概念)
class Student:
    school = "北京林业大学"
    print(1)
    def learn(self):
        print("is learning")
    def eat(self):
        print("is eating")

#后产生对象(实例化)
stu1 = Student()
print(stu1)

