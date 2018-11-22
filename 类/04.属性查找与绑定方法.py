# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 10:09
# @Author  : ways
# @Email   : 1076377207@qq.com
# @File    : 04.属性查找与绑定方法.py
class Student:
    school = "北京林业大学"
    def __init__(self,name,sex,age):  # 实例化对象自动调用
        self.name = name
        self.sex = sex
        self.age = age
        # stu1.name = "ways"
        # stu1.sex = "女"
        # stu1.age = 18
    def learn(self):
        print("is learning")
    def eat(self):
        print("is eating")
stu1 = Student("ways1","男",18)
stu2 = Student("ways2","男",18)
stu3 = Student("ways3","男",18)
# 对象：特征与技能的结合体
# 类：一些列相似的特征与相似的技能的结合体


# 类中的数据属性：是所有对象共有的
print(Student.school,id(Student.school))
print(stu1.school,id(stu1.school))
print(stu2.school,id(stu2.school))
print(stu3.school,id(stu3.school))
# 类中的函数属性：是绑定给对象使用的，绑定到不同的对象是不同的绑定方法，我吃完东西是你吃了吗？，内存地址不同,id相同,对象调用绑定方法时，会把对象本身当作第一个参数传入给self
# ps: id是python的实现机制,并不能真实反映内存地址,如果有内存地址,还是以内存地址为准
print(Student.eat)
print(stu1.eat,id(stu1.eat))
print(stu2.eat,id(stu2.eat))
print(stu3.eat,id(stu3.eat))
print(stu1.eat)
stu1.eat()    # eat(stu1)