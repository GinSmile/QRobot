# -*- coding: utf-8 -*-
import os
import random

#遍历images文件夹下的所有文件，随机选择一个
def pic():
    f = ()
    for f in os.walk(r'../res/images/'):
        pass
    filename = f[2][random.choice(range(len(f[2])))]
    myPic = open('../res/images/' + filename, 'rb')
    return myPic