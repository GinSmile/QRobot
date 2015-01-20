# -*- coding: utf-8 -*-
import random
import urllib2
import json
import re

#吐槽函数
def hello(hour):
	if hour == 23:
		return "こんばんは~~ご主人さま~"
	else:
		#myfile = open('../../res/greet.txt','rU')
		myfile = open('../res/greet.txt','rU')
		lines = {}
		lines = myfile.readlines()
		index = random.choice(range(len(lines) - 1))
		return lines[index]

def comment():
	myfile = open('../res/comment.txt','rU')
	lines = {}
	lines = myfile.readlines()
	index = random.choice(range(len(lines) - 1))
	return lines[index]