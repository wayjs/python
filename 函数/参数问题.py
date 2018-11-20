# -*- coding: utf-8 -*-
# @Time    : 2018/11/19 9:58
# @Author  : ways
# @Email   : 1076377207@qq.com
# @File    : 参数问题.py


def stu_info(name,age, cn="china",*args, **kwargs):
    print("姓名：", name)
    print("年龄：", age)
    print("国籍：", cn)
    print("非固定参数1：：", args)
    print("非固定参数2：：", kwargs)


stu_info("ways",18,grade=80,)
