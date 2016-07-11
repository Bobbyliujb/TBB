#!/usr/bin/env python
#-*- coding:utf-8 -*-

import json
import MySQLdb

# register and login
def ifExistUser(username):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    cur.execute('select * from users where username = \"' + username + '\"')
    arr = cur.fetchall()
    cur.close(); cxn.close()
    return len(arr)>0

def verifyPassword(username, password):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    cur.execute('select * from users where username = \"' + username + '\"')
    arr = cur.fetchall()
    cur.close(); cxn.close()
    print arr
    return arr[0][2] == password

def addUser(username, password, nickname, headurl):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    cur.execute('insert into users (username, password, nickname, headurl)\
        values (\"'+username+'\", \"'+password+'\", \"'+nickname+'\", \"'+headurl+'\")')  
    cur.close(); cxn.commit(); cxn.close()

# Update personal information
def updatePassword(username, password):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    cur.execute('update users set password = \"'+password+'\" where username = \"'+username+'\"')
    cur.close(); cxn.commit(); cxn.close()

def updateNickname(username, nickname):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    cur.execute('update users set nickname = \"'+nickname+'\" where username = \"'+username+'\"')
    cur.close(); cxn.commit(); cxn.close()

def updateHeadurl(username, head):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    cur.execute('update users set headurl = \"'+head+'\" where username = \"'+username+'\"')
    cur.close(); cxn.commit(); cxn.close()

def updateMessage(username, college, qq, grade, phone):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    # cur.execute("set names utf8")
    cur.execute('update users set college = \"'+college+'\", qq = \"'+qq+'\", grade = \"' \
        +grade+'\", phone = \"'+phone+'\"'+' where username = \"'+username+'\"')
    cur.close(); cxn.commit(); cxn.close()
    
def getMessage(username):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    cur.execute('select * from users where username = \"' + username + '\"')
    arr = cur.fetchall()
    cur.close(); cxn.close()
    return arr

# Operations for item type
def ifTypeExist(name):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    cur.execute('select * from type where typename = \"' + name + '\"')
    arr = cur.fetchall()
    cur.close(); cxn.commit(); cxn.close()
    return len(arr)>0

def addType(name, text=""):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    cur.execute('insert into type (typename, typetext) values \
        (\"' + name + '\", \"' + text + '\")')
    cur.close(); cxn.commit(); cxn.close()
    
def getType(name):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    cur.execute('select typetext from type where typename = \"' + name + '\"')
    arr = cur.fetchall()
    cur.close(); cxn.commit(); cxn.close()
    return arr[0][0] 

def updateType(name, text):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    cur.execute('update type set typetext = \"' + text + '\" where typename = \"' + name + '\"')
    cur.close(); cxn.commit(); cxn.close()

def delType(name):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    cur.execute('delete from type where typename = \"' + name + '\"')
    cur.close(); cxn.commit(); cxn.close()

# Operations for items
def ifItemExist(item_id):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    cur.execute('select * from items where item_id = ' + item_id + '')
    arr = cur.fetchall()
    cur.close(); cxn.commit(); cxn.close()
    return len(arr)>0

def getItemId(name, text, time, price):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    cur.execute('select item_id from items where item_name = \"' + name + '\" and ' \
         'item_text = \"' + text + '\" and item_time = \"' + time + '\" and item_price = \"'+ price +'\"')
    arr = cur.fetchall()
    cur.close(); cxn.commit(); cxn.close()
    if not len(arr):
        return -1
    else:
        return arr[0][0]

def addItem(name, text, time, price):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    cur.execute('insert into items (item_name, item_text, item_time, item_price) values \
        (\"' + name + '\", \"' + text + '\", \"' + time + '\", \"' + price + '\")')
    cur.execute('select item_id from items where item_name = \"' + name + '\" and ' \
         'item_text = \"' + text + '\" and item_time = \"' + time + '\" and item_price = \"'+price+'\"')
    arr = cur.fetchall()
    cur.close(); cxn.commit(); cxn.close()
    return arr[0][0]

def addItemFromUser(item_id, username):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    cur.execute('insert into item_from_user (item_id, username) values \
        (' + item_id + ', \"' + username + '\")')
    cur.close(); cxn.commit(); cxn.close()
    
def addItemToType(item_id, typename):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    cur.execute('insert into item_to_type (item_id, typename) values \
        (' + item_id + ', \"' + typename + '\")')
    cur.close(); cxn.commit(); cxn.close()
    
def getItem(item_id):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    cur.execute('select * from items where item_id = ' + item_id + '')
    arr = cur.fetchall()
    cur.close(); cxn.commit(); cxn.close()
    if not len(arr):
        return -1
    else:
        return arr[0]
   
def getItemFromUser(item_id):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    cur.execute('select username from item_from_user where item_id = ' + item_id + '')
    arr = cur.fetchall()
    cur.close(); cxn.commit(); cxn.close()
    return arr[0][0]

def getItemToType(item_id):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    cur.execute('select typename from item_to_type where item_id = ' + item_id + '')
    arr = cur.fetchall()
    cur.close(); cxn.commit(); cxn.close()
    return arr[0][0]
    
def delItem(item_id):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    cur.execute('delete from items where item_id = ' + item_id + '')
    cur.close(); cxn.commit(); cxn.close()
   
def delItemFromUser(item_id):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    cur.execute('delete from item_from_user where item_id = ' + item_id + '')
    cur.close(); cxn.commit(); cxn.close()

def delItemToType(item_id):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    cur.execute('delete from item_to_type where item_id = ' + item_id + '')
    arr = cur.fetchall()
    cur.close(); cxn.commit(); cxn.close()
     
def updateItem(item_id, name, text, time, price):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    cur.execute('update items set item_name = \"' + name + '\", ' \
         'item_text = \"' + text + '\", item_time = \"' + time + '\", item_price = \"'\
         + price+'\" where item_id = '+item_id)
    cur.close(); cxn.commit(); cxn.close()

def updateItemFromUser(item_id, username):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    cur.execute('update item_from_user set username = \"'+username+'\" where item_id = '+item_id)
    cur.close(); cxn.commit(); cxn.close()
    
def updateItemToType(item_id, typename):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    cur.execute('update item_to_type set typename = \"'+typename+'\" where item_id = '+item_id)
    cur.close(); cxn.commit(); cxn.close()

def ifBuyed(item_id):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    cur.execute('select buy_flag from items where item_id = '+item_id)
    arr = cur.fetchall()
    cur.close(); cxn.commit(); cxn.close()
    return arr[0][0]==1

def getSellingItems(username):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    c = cxn.cursor(MySQLdb.cursors.DictCursor)
    cur.execute('select item_id from (items A natural join item_from_user B) where B.username != \"'+username+'\" and A.buy_flag = 0' )
    # cur.execute('select item_id from items where buy_flag = 0')
    arr = cur.fetchall()
    dic = {}
    string = ''
    for i in xrange(len(arr)):
        string += str(arr[i][0])+'/'
    dic['item_num'] = len(arr); dic['item_list'] = string
    return dic

def getOwnItems(username):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    c = cxn.cursor(MySQLdb.cursors.DictCursor)
    cur.execute('select item_id from (items A natural join item_from_user B) where B.username = \"'+username+'\"')
    arr = cur.fetchall()
    dic = {}
    string = ''
    for i in xrange(len(arr)):
        string += str(arr[i][0])+'/'
    dic['item_num'] = len(arr); dic['item_list'] = string
    return dic

def getUserItems(username):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    c = cxn.cursor(MySQLdb.cursors.DictCursor)
    cur.execute('select item_id from (items A natural join item_from_user B) where B.username = \"'+username+'\" and A.buy_flag = 0')
    arr = cur.fetchall()
    dic = {}
    string = ''
    for i in xrange(len(arr)):
        string += str(arr[i][0])+'/'
    dic['item_num'] = len(arr); dic['item_list'] = string
    return dic


# image
def addItemUrl(item_id):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    cur.execute('update items set imageurl = \"' + item_id+'_image.png' + '\"' + 'where item_id = ' + item_id)
    cur.close(); cxn.commit(); cxn.close()

# buyer item    
def buyItem(item_id):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    cur.execute('update items set buy_flag = 1 where item_id = '+item_id)
    arr = cur.fetchall()
    cur.close(); cxn.commit(); cxn.close()

def addItemForUser(item_id, username):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    cur.execute('insert into item_for_user (item_id, username) values \
        (' + item_id + ', \"' + username + '\")')
    cur.close(); cxn.commit(); cxn.close()
           
def getBuyer(item_id):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    cur.execute('select username from item_for_user where item_id = '+item_id)
    arr = cur.fetchall()
    cur.close(); cxn.commit(); cxn.close()
    if len(arr)==0:
        return -1
    else:
        return arr[0][0]

# resell item    
def resellItem(item_id):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    cur.execute('update items set buy_flag = 0 where item_id = '+item_id)
    arr = cur.fetchall()
    cur.close(); cxn.commit(); cxn.close()

def delItemForUser(item_id, username):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    cur.execute('delete from item_for_user where item_id = '+item_id)
    cur.close(); cxn.commit(); cxn.close()

def getSeller(item_id):
    cxn = MySQLdb.connect("localhost", "root", "smie", "tbb", charset="utf8")
    cur = cxn.cursor()
    cur.execute('select username from item_from_user where item_id = '+item_id)
    arr = cur.fetchall()
    cur.close(); cxn.commit(); cxn.close()
    if len(arr)==0:
        return -1
    else:
        return arr[0][0]



