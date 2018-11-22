# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 9:32
# @Author  : ways
# @Email   : 1076377207@qq.com
# @File    : 03.对象的使用.py
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
stu1 = Student("ways","男",18)

# 加上__init__方法后，实例化步骤
#1、先产生一个空对象
#2、Student.__init__(stu1,"ways","男",18)
print(stu1.__dict__)   # 命名空间
# 查
print(stu1.age)
# 改
stu1.age = 20
print(stu1.age)
# 删
del stu1.age
print(stu1.__dict__)
# 增
stu1.class_name = "python全栈"
print(stu1.__dict__)