#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
import sys
def init():
    getroot()
    global filepath
    filepath=os.getcwd()
    global apppath
    apppath=raw_input('please input your webapp path(defauult:/var/www)')
    if apppath=='':
        apppath='/var/www/'
def install():
    os.system('tar -zxvf php_screw-1.5.tar.gz')
    os.chdir('php_screw-1.5')
    fileedit('php_screw.h',0,"#define PM9SCREW        \""+"guoyun"+"\"\n")
    fileedit('php_screw.h',1,"#define PM9SCREW_LEN     "+"6"+'\n')
    os.system('phpize')
    os.system('./configure --with-php-config=/usr/bin/php-config')
    fileedit('php_screw.c',123,'\tCG(compiler_options) |= ZEND_COMPILE_EXTENDED_INFO;\n')
    fileedit('php_screw.c',132,'\tCG(compiler_options) |= ZEND_COMPILE_EXTENDED_INFO;\n')
    os.system('make')
    os.system('make install')
def config():
    output=open('/etc/php5/apache2/php.ini','a')
    output.write('extension=/php_screw.so')
    output.close()
def insscrew():
    os.chdir(filepath+'/php_screw-1.5/tools')
    os.system('make')
    os.system('mv screw /opt/')
    os.system('ln -s /opt/screw /usr/bin/screw')
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
            os.remove(f+'.screw')
    os.chdir('..')
def encryptwebsite():
    os.chdir(filepath)
    os.system('mv webapp '+apppath)
    os.system('chmod 777 -R '+apppath+'"webapp"')
def getroot():
    if os.getuid():
        print 'root password:'
        args=[sys.executable]+sys.argv
        os.execlp('su','su','-c',' '.join(args))
def clean():
    os.system("rm -r "+filepath+" ")
def fileedit(fname,line,ncontent):
    ufile=open(fname,'r+')
    update=ufile.readlines()
    update[line]=ncontent
    ufile=open(fname,'w+')
    ufile.writelines(update)
    ufile.close()
if __name__=='__main__':
    init()
    install()
    config()
    os.system('service apache2 restart')
    insscrew()
    encrypt(filepath+'/webapp')
    encryptwebsite()
    clean()
