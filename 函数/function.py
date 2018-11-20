# -*- coding: utf-8 -*-
# @Time    : 2018/11/19 9:18
# @Author  : ways
# @Email   : 1076377207@qq.com
# @File    : function.py
# class A:
#     def __init__(self,grade):
#         self.grade = grade
#
#     def print_grade(self):
#         print(self.grade)
# a = A(49)
# a.print_grade()

li = [lambda: x for x in range(10)]
print(type(li),li[1]())
res = li[0]()
print(res)
for i in li:
    print(i())