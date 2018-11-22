# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 14:36
# @Author  : ways
# @Email   : 1076377207@qq.com
# @File    : 07.继承与重用.py

""""
继承是类与类之间的关系，是一种什么“是”什么的关系，继承的功能之一就是用来解决代码重用问题
"""


class People:
    def __init__(self, name, sex, age):
        self.name = name
        self.age = age
        self.sex = sex


class Student(People):

    # def __init__(self,name, sex, age, grade):
    #     self.name = name
    #     self.age = age
    #     self.sex = sex
    #     self.grade = grade

    def study(self):
        print("%s is studying" % self.name)


class Teacher(People):

    # def __init__(self, name, sex, age, teach_class):
    #     self.name = name
    #     self.sex = sex
    #     self.age =age
    #     self.teach_class = teach_class

    def teach(self):
        print("%s is teaching" % self.name)


stu = Student("ways", "male", 13)
print(stu.name)
#  查看继承 #__base__只查看从左到右继承的第一个子类，__bases__则是查看所有继承的父类
print(Teacher.__bases__)
print(Teacher.__base__)



# 小练习题目
# self ,谁调用，self,指的就是谁  属性查找顺序：1.对象__init__ 2.自己的类中 3.父类

class Foo:
    def f1(self):
        print("from Foo.f1")
    def f2(self):
        print("from Foo.f2")
        self.f1()
class Bar(Foo):
    def f1(self):
        print("from Bar.f1")
b = Bar()
b.f2()