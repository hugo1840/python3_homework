#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

def findKeyFiles(dirPath, keyStr):
	for f in os.listdir(dirPath):
		fpath = os.path.join(dirPath, f)
		if os.path.isdir(fpath):
			findKeyFiles(fpath, keyStr)
		else:
			fname = os.path.split(fpath)
			if keyStr in fname[1]:
				print(fpath)


#dirPath = 'D:\\PyWorkplace\\'
#findKeyFiles(dirPath, 'test')

# 当前目录下查找
#findKeyFiles('.','tr')

# 命令行传参： python findKeyFiles.py test
if __name__ == "__main__":
    findKeyFiles('.', sys.argv[1])
    