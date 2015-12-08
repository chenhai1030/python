#!/usr/bin/env python

import os
import sys 
import argparse
import sqlite3

description = '''usage: [-s srcdb] [-d dstdb] [-t table]

This is the tool for merge sqlite database
Run it like this:
    python merge_db.py -s srcdb -d dstdb -t table'''

parser = argparse.ArgumentParser(description)
parser.add_argument('-s','--srcdb',help='source database')
parser.add_argument('-d','--dstdb',help='destination database')
parser.add_argument('-t','--table',help='table in database')
args=parser.parse_args()


def get_conn(path):
    '''Get the particular database handle'''
    if os.path.exists(path) and os.path.isfile(path):
        conn = sqlite3.connect(path)
    else:
        conn = None
    return conn

def get_cursor(conn):
    '''Get the cursor of db we connected'''
    if conn is not None:
        cur = conn.cursor()
    else:
        print "The db cant be connected, please check!"
        exit()
    return cur
    

def check_params():
    '''Check if the parameters is correct'''
    print "check"

def cover_db(srcdb, dstdb, table):
    conn = get_conn(args.dstdb)
    cur = get_cursor(conn)

    #step 1: attach src database
    attach = 'attach database "'+srcdb+'" as srcdb;'
    cur.execute(attach) 
    #step 2: delete the dstination database table inorder to 
    #print ("command tmp=%s" %(attach))
    delete = 'delete from "'+table+'";'
    cur.execute(delete)
    #step 3: insert table from source DB
    insert ='insert into "'+table+'" select * from srcdb."'+table+'";'
    cur.execute(insert)
    
    conn.commit()
    conn.close()



def main(argv):
    result = 0

    print ("the argv is src=%s and dst=%s  tab=%s" %(args.srcdb, args.dstdb, args.table))
    cover_db(args.srcdb, args.dstdb, args.table)

    sys.exit(result)

if __name__ == '__main__':
    main(sys.argv[1:])
