#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/11 11:53 下午 
# @Author :laixiaobin
# @File : function_test.py

def method(a,b=[]):
    b.append(a)
    return b

print(method(1))
print(method(2))   