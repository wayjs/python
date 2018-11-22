# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 23:53
# @Author  : ways
# @Email   : 1076377207@qq.com
# @File    : 16.自定义元类控制类的实例化行为.py


class Mymeta(type):    # 重写一部分type元类
    def __init__(self,class_name,class_bases,class_dic):
        if not class_name.istitle():
            raise TypeError("类型的首字母必须大写")
        if "__doc__" not in class_dic or not class_dic["__doc__"].strip():
            raise TypeError("必须有注释，且注释不能为空")
        # print(class_name)
        # print(class_bases)
        super(Mymeta,self).__init__(class_name,class_bases,class_dic)

    def __call__(self, *args, **kwargs):
        # print(self)
        # print(args)
        # print(kwargs)
        #1.造出一个空对象
        obj = object.__new__(self)
        #2.初始化obj  用People 类中的__init__ 在这里self 就是People
        self.__init__(obj,*args,**kwargs)
        #3.返回值
        return obj
class People(object,metaclass=Mymeta):   # metaclass 元类，默认是type
    """ddd"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("is eating")


obj = People("ways",18)    # People.__call__(People,"ways",18)
"""
知识储备：__call__方法
元类内部也有一个__call__方法，会在调用People时触发执行
People("ways",18) 等价为：People.__call__(People,"ways",18)
"""
print(obj.__dict__)