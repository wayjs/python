# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 15:26
# @Author  : ways
# @Email   : 1076377207@qq.com
# @File    : 08.派生,子类中重用父类属性.py

"""
当然子类也可以添加自己新的属性或者在自己这里重新定义这些属性（不会影响到父类），需要注意的是，
一旦重新定义了自己的属性且与父类重名，那么调用新增的属性时，就以自己为准了。
"""
# class People:
#     def __init__(self, name, sex, age):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def eat(self):
#         print("吃饭中。。。。")
#
# # 方式一：指名道姓的方式，不依赖继承
# # 方式二：super(),依赖继承,依赖mro列表，就根据mro列表往后找
# class Student(People):
#
#     def __init__(self,name, sex, age, grade):
#         # self.name = name
#         # self.age = age
#         # self.sex = sex
#         #指名道姓
#         # People.__init__(self.name,sex,age)
#         #方式二：super()  python3 可以简写为super()
#         super(Student,self).__init__(name,sex,age)
#         self.grade = grade
#
#     def study(self):
#         print("%s is studying" % self.name)
#
#     def eat(self):
#         People.eat(self)  # 指名道姓，不依赖继承
#         super(Student,self).eat() # 依赖继承，得到的父类对象，调用绑定方法，不是函数了
#         print("%s is eating" % self.name)
#
#
# class Teacher(People):
#
#     def __init__(self, name, sex, age, teach_class):
#         self.name = name
#         self.sex = sex
#         self.age =age
#         self.teach_class = teach_class
#
#     def teach(self):
#         print("%s is teaching" % self.name)

class A:
    def __init__(self, name, sex, age, grade):
        self.name = name
        self.age = age
        self.sex = sex
        self.grade = grade

class People:
    def __init__(self, name, sex, age):
        self.name = name
        self.age = age
        self.sex = sex

    def eat(self):
        print("吃饭中。。。。")


class Student(People, A):
    def __init__(self,name, sex, age, grade):

        print(super().__init__)

    def study(self):
        print("%s is studying" % self.name)

stu = Student("wsy", "male", 14,"二班")
print(stu.eat())

