# -*- coding: utf-8 -*-
# @Time    : 18-3-13 下午4:16
# @Author  : Yan
# @Site    : 
# @File    : env_spr.py
# @Software: PyCharm Community Edition
# @Function: A SPR game environment
# @update:
import numpy
import os
import datetime

# # time record
# starttime = datetime.datetime.now()
class Env():

    def __init__(self):
        self.action = ['scissor','paper','rock']
        self.result = ['win','loss','due']

    def rule(self,action0,action1):

        if action0 in self.action and action1 in self.action:
            if action0 == action1:
                return self.result[2]
            if action0 == self.action[0]:
                if action1 == self.action[1]:
                    return self.result[0]
                else:
                    return self.result[1]
            elif action0 == self.action[1]:
                if action1 == self.action[0]:
                    return self.result[1]
                else:
                    return self.result[0]
            else:
                if action1 == self.action[0]:
                    return self.result[0]
                else:
                    return self.result[1]
        else:
            raise Exception("Run input action!")


