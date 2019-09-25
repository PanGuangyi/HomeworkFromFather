#!/usr/bin/env python3

import sys

import tasks.Homework as hw
from tasks.Math_TuiWeiJianFa import Math_TuiWeiJianFa
from tasks.Math_FuHaoShiBie import Math_FuHaoShiBie
from tasks.Math_ShuZiShuXie import Math_ShuZiShuXie



class HomeworkCreator():
    
    def __init__(self,task_name):
    
        #register home work
        hw.factory.register_homework(task_name,eval(task_name))        

        if hw.factory.is_homework_exist(task_name):
            myhomework = hw.factory.get_homework(task_name)
            myhomework.create_homework()
        else:
            print(task_name+"不存在！")


