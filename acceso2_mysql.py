#!/usr/bin/python
import os
import sys
usuario=marisa
password=marisa
bd=empresa
##print("mysql --user " + usuario + " -p " + contrasena + " " + bd)
os.system('mysql -u ' +usuario+ ' -p' +password+ ' ' + bd)
