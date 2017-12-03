#!/usr/bin/python
import os
import sys
usuario=sys.argv[1]
password=sys.argv[2]
bd=sys.argv[3]
##print("mysql --user " +usuario+ " -p" +password+ " " +bd)
os.system('mysql -u ' +usuario+ ' -p' +password+ ' ' +bd)