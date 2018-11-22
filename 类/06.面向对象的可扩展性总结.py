# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 13:58
# @Author  : ways
# @Email   : 1076377207@qq.com
# @File    : 06.面向对象的可扩展性总结.py
# 将数据与专门操作该数据的功能整合到一起
# 可扩展性高


class Student:
    count = 0
    def __init__(self,name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        Student.count += 1

    def learn(self):
        print("%s is learning" % self.name)

stu1 = Student("ways1",12,"male")
print(stu1.count)
stu2 = Student("ways2",12,"male")
print(stu2.count)
stu3 = Student("ways3",12,"male")
print(stu3.count)