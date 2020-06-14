#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/14 12:44 下午 
# @Author :laixiaobin
# @File : 7_输入与输出.py

import json

info = [
    {
        "name":"Jack",
        "age":18
    },
    {
        "name":"John",
        "age":24
    }
]

data = json.dumps(info,sort_keys=True,indent=4)
print(data)
print(type(data))

json.dump(info,open('datas/textfile','w'),sort_keys=True,indent=4)

info2 = '''[
    {
        "name":"Jack",
        "age":28
    },
    {
        "name":"Jhon",
        "age":28
    }
]'''

# 字符串转json
data2 = json.loads(info2)
print(data2)
print(type(data2))

jsObj = json.load(open('datas/test.json','r'))
print(jsObj)
print(type(jsObj))
















