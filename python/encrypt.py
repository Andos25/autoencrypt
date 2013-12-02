#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
import sys
def encrypt(serveDir):
	path=serveDir
	os.chdir(serveDir)
	files=os.listdir(serveDir)
	for f in files:
		if os.path.isdir(f):
			encrypt(path+'/'+f)
			print 'open director:'+path+'/'+f
		elif f[len(f)-4:len(f)]=='.php':
			print 'encrypt:'+path+'/'+f
			os.system('screw '+f)
	os.chdir('..')
if os.getuid():
	print '请输入root密码'
	args=[sys.executable]+sys.argv
	os.execlp('su','su','-c',' '.join(args))
encrypt('/usr/local/apache2/htdocs')
