# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 23:20
# @Author  : ways
# @Email   : 1076377207@qq.com
# @File    : 20.绑定方法和非绑定方法的使用.py
import settings
import hashlib
import time

class People:

    def __init__(self, name, age, sex):
        self.id = self.creat_id()
        self.name = name
        self.age = age
        self.sex = sex

    def tell_info(self):     # 根据函数体的逻辑，判断使用什么类型的方法
        print("name:%s age:%s sex:%s" % (self.name, self.age, self.sex))

    @classmethod
    def from_conf(cls):
        obj = cls(settings.name,settings.age,settings.sex)
        return obj

    @staticmethod
    def creat_id():
        m = hashlib.md5(str(time.time()).encode("utf-8"))
        return m.hexdigest()



p = People("ways", 13, "male")
# 绑定给对象，就应该由对象本身来调用，自动将对象本身当作第一个参数传入
p.tell_info()
# 需求：从配置文件中读取信息
# 绑定给类，就应该由类来调用，自动将类本真当作第一个参数传入
p2 = People.from_conf()    # from_conf(People)
p2.tell_info()
# 非绑定方法，不与类或者对象绑定，谁都可以调用没有自动传值一说

p3 = People("ways1",19,"male")
time.sleep(1)
p4 = People("ways2",19,"male")
time.sleep(2)
p5= People("ways3",19,"male")
print(p3.id)
print(p4.id)
print(p5.id)


