#!/bin/bash
filepath=$(cd "$(dirname "$0")"; pwd)
Extract()
{
    filepath=$(cd "$(dirname "$0")"; pwd)
    tar zxvf $filepath"/php_screw-1.5.tar.gz"
    php_screw_path=$filepath"/php_screw-1.5"    
}

Install()
{
    cd $php_screw_path
    phpize
    sed -i 's/^#define PM9SCREW .*$/#define PM9SCREW "GUOYUNDATA"/g' php_screw.h
    ./configure --with-php-config=/usr/bin/php-config 
    sed -i 's/CG(extended_info) = 1;/CG(compiler_options) |= ZEND_COMPILE_EXTENDED_INFO;/g' php_screw.c
    sudo make
    sudo make install
}

CreateLink()
{
    cd $php_screw_path"/tools"
    make
    sudo mv screw /opt/ 
    sudo ln -s /opt/screw /usr/bin/screw
}

Encrypt()
{
    cd $filepath
    python encrypt.py
}

EncryptWebsite(){
    cd $filepath
    echo "please input your web root path, (default: /var/www/)"
    read path
    if [ "$path" = "" ];then
        path="/var/www/"
    fi
    sudo mv webapp $path
    sudo chmod 777 -R $path"webapp"
    path=$path"webapp"
}

Clean()
{
    cd $filepath
    sudo rm -r * $filepath
}

Extract
Install
CreateLink
Encrypt
EncryptWebsite
Clean
