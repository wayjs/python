# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 9:24
# @Author  : ways
# @Email   : 1076377207@qq.com
# @File    : 02.类的使用.py
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
print(Student.__dict__)
print(stu1.__dict__)
#查属性
print(Student.school)
print(Student.learn)
# 增
Student.country = "China"
print(Student.__dict__)
# 删除
del Student.country
# 改
Student.school = "LuffyCity"
print(Student.school)
