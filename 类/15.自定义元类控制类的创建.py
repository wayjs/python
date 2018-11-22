# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 23:31
# @Author  : ways
# @Email   : 1076377207@qq.com
# @File    : 15.自定义元类控制类的创建.py


class Mymeta(type):    # 重写一部分type元类
    def __init__(self,class_name,class_bases,class_dic):
        if not class_name.istitle():
            raise TypeError("类型的首字母必须大写")
        if "__doc__" not in class_dic or not class_dic["__doc__"].strip():
            raise TypeError("必须有注释，且注释不能为空")
        # print(class_name)
        # print(class_bases)
        super(Mymeta,self).__init__(class_name,class_bases,class_dic)


class People(object,metaclass=Mymeta):   # metaclass 元类，默认是type
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("is eating")

