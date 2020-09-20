#!/usr/bin/python

import os



#backup_file = "/home/me/Cloud.7z"
backup_file = "/home/me/tmp/Cloud.7z"
backup_dir = "/home/me/lab/"
backup_cmd = '"7z a -t7z -mx=9 -mfb=64 -md=32m -ms=on" + backup_file + backup_dir'



if os.path.isfile(backup_file):
    print ("File exist")
    os.remove(backup_file)
    print ("File deleted")
    os.system(backup_cmd)
    print ("Backup created")
else:
    print ("File not exist")
    os.system(backup_cmd)
    print ("Backup created")