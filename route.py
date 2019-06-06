#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#This file was created to remove files of a specific path using os library


import os

route1 = 'C:\\Users\\Gustavo Paez\\Documents\\05_Trash\\x\\r\\demofile.txt'
route2 = 'D:\\git1\\cfcn-vwfc-mx\\bi-system-workflow\\00_Release\\02_Release_Implementation\\04_DB_Scripts\\'

#if os.path.exists('C:\\Users\\Gustavo Paez\\Documents\\05_Trash\\x\\r\\demofile.txt'):
#os.remove('C:\\Users\\Gustavo Paez\\Documents\\05_Trash\\x\\r\\demofile.txt')
if os.listdir(path=route2):   
    #os.remove(route2 + '*.sql')
    print("not empty")
    filelist = [ f for f in os.listdir(path=route2) ]#if f.endswith(".sql")] #Only sql files
    for f in filelist:
        os.remove(route2 + f)
    print("files removed")
    
else:
    print("empty")
