#!/usr/bin/env python3

import sys

import Homework as hw
from Math_TuiWeiJianFa import Math_TuiWeiJianFa
from Math_FuHaoShiBie import Math_FuHaoShiBie
from Math_ShuZiShuXie import Math_ShuZiShuXie



if __name__ == '__main__':
    
    #register home work
    hw.factory.register_homework("Math_TuiWeiJianFa",Math_TuiWeiJianFa)
    hw.factory.register_homework("Math_FuHaoShiBie",Math_FuHaoShiBie)
    hw.factory.register_homework("Math_ShuZiShuXie",Math_ShuZiShuXie)
    
    
    for item in sys.argv[1:]:
        if hw.factory.is_homework_exist(item):
            myhomework = hw.factory.get_homework(item)
            myhomework.create_homework()
        else:
            print(item+"不存在！")
    
    
