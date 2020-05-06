#!/usr/bin/python3


"""
Usage: ohsnap.py database.db {usually main.db or tcpahn.db)

Antiskurken

"""

import sqlite3 as sql, sys as argv, xlswriter

def get_account(queryList):
    for item in queryList:
         user = item[0]
    return user

    
	
def connect_db(query):
    connect = sql.connect('main.db')
    cursor = connect.cursor()
    with connect:
        if query == 'snaptoken':
            cursor.execute("Select Friend.username from Snaptoken inner join Friend on SnapToken.userId=Friend.userId")
            queryList = cursor.fetchall()
        return get_account(queryList)
        cursor.close()

def connect_db2(query):
    connect = sql.connect('main.db')
    cursor = connect.cursor()
    with connect:
        if query == 'msg':
            cursor.execute("select datetime(message.timestamp / 1000, 'unixepoch', 'localtime') as Tid, datetime(message.seenTimestamp / 1000, 'unixepoch', 'localtime') as Tid_sedd, message.content as Meddelande, message.type as Typ_av_meddelande, message.savedStates, message.screenshottedOrReplayed, message.lastInteractionTimestamp, Friend.username from message inner join Friend on Message.senderId=Friend._id")
            queryList = cursor.fetchall()
        return get_message(queryList)
        cursor.close()


#connect_db('snaptoken')
connect_db2('msg')

    



