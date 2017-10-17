#coding:utf8

import os
from itertools import islice  
import json

# 遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):

	hasFound=False
	for root,dirs,names in os.walk(filepath):
		for filename in names:
			if 'findpaul' in filename:
				break
			fullfilename=os.path.join(root,filename)#路径和文件名连接构成完整路径
			#if 'o.' in filename:
				#print '-----------------------------'
				#break
			with open(fullfilename,'r') as f:
				if 'maps' in fullfilename:
						break
				print 'searching %s ...'% fullfilename
				
				for line in islice(f, 0, None):  
					if 'weapon' in line:
						print 'file name: %s ...' % fullfilename
						print '    "%s" ' % line
						raw_input()

				# js=json.loads(fff)
				# print js['npcs']
				# print 'loading %s ...' % fullfilename 
		if hasFound:
			break

# 读取文件内容并打印
def readFile(filename):
	fopen = open(filename, 'r') # r 代表read
	for eachLine in fopen:
		print "读取到得内容如下：",eachLine
	fopen.close()

eachFile('../../')
#eachFile('maps')
    