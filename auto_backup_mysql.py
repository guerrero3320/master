#!/usr/bin/python
import os

nombre = raw_input("Introduzca usuario: ")
password = raw_input("Introduzca la clave: ")
bd = raw_input("Introduzca el nombre de la Base de Datos: ")

os.system('mysqldump -u '+nombre+' -p'+password+' '+bd+' > backup_empresa.sql')
