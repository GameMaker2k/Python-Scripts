#!/bin/sh

if [ ! -f "/usr/bin/python2" ];then
	/usr/bin/python "./bin/clock.py" $* > "./stdout.txt"
else
	/usr/bin/python2 "./bin/clock.py" $* > "./stdout.txt"
fi
