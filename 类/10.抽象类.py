# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 19:55
# @Author  : ways
# @Email   : 1076377207@qq.com
# @File    : 10.抽象类.py
import abc


class All_file(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def read(self):
        pass
    @abc.abstractmethod
    def write(self):
        pass

class Txt(All_file):
    def read(self):
        print("文本数据读取方式")
    def write(self):
        print("文本数据的读取方式")


class Sate(All_file):
    def read(self):
        print("硬盘数据的读取方式")
    def write(self):
        print("硬盘数据的读取方式")
wenben = Txt()
wenben.read()
sate = Sate()
sate.read()