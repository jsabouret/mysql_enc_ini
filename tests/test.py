#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import argparse
from mysql_enc_ini import Mysql_enc_ini
import mysql.connector



def args_list():
  parse = argparse.ArgumentParser('connect to mysql tools')
  parse.add_argument("-H","--host",dest='hostname',action='store',default='localhost',help='mysql server hostname.')
  parse.add_argument("-u","--user",dest='username',action='store',default='root',help='connect to mysql server user.')
  parse.add_argument("-d","--db",dest='database',action='store',default='mysql',help='Database name.')
  parse.add_argument("-P","--port",dest='port',action='store',default='3306',help='Port number.')
  parse.add_argument("-D","--debug",type=int,dest='debug',action='store',default=0,help='Debugging mode.')
  args = parse.parse_args()
  return args

kvargs = {}
args = args_list()
kvargs["hostname"] = args.hostname
kvargs["username"] = args.username
kvargs["database"] = args.database
kvargs["debug"] = args.debug
kvargs["port"] = args.port

pwdfile = kvargs["hostname"] + "_" + kvargs["database"] + "_" + kvargs["username"] + ".pwd"
connect = Mysql_enc_ini(**kvargs)
#connect = Mysql_enc_ini()
conn_data = connect.decrypt(pwdfile)
dbh = mysql.connector.connect(**conn_data)
mycursor=dbh.cursor()
mycursor.execute("SHOW DATABASES")
myresult = mycursor.fetchall()
for row in myresult:
  print(row[0])
mycursor.close()
dbh.close()
# You can of course configure the file directly with
# where mysql.ini is the unencrypted connection file (must not exists) and the destination file

#connect.encrypt("mysql.ini","mysql_enc.ini")
