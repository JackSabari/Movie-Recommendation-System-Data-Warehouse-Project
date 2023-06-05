# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 17:44:08 2023

@author: Sabari
"""

import pymysql

print('Movie Recommendation System\n')

def create_user_db():
    connection_db = pymysql.connect(
            host='localhost',
            user='root', 
            password = "root",
            )
          
    cur = connection_db.cursor()
      
    # Select query
    cur.execute("create database userdb")
      
    # To close the connection
    connection_db.close()

create_user_db()    
    