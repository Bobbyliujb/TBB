#!/usr/bin/env python
#-*- coding:utf-8 -*-

import web, json, os
from rescode import *
from attributes import *
from dbop import *

urls = (
    "/sign_up", "SignUp",
    "/sign_in", "SignIn",
    "/pict", "Pict",
    "/personal_msg", "Message",
    "/item_type", "Type",
    "/seller", "Seller",
    "/buyer", "Buyer",
)

request = 'request'
rescode = 'rescode'
pict_dir = '../head/'
head_dir = '../picture/'

class SignUp:
    def GET(self):
        para = web.input()
        if not username in para:
            return json.dumps({rescode:PARA_ERROR})
        else:
            try:
                if username not in para or password not in para \
                    or nickname not in para:
                    return json.dumps({rescode:PARA_ERROR})
                elif ifExistUser(para[username]):
                    return json.dumps({rescode:USER_EXIST})
                else:
                    # The hear image url is defaultly plus '_head.png'
                    addUser(para[username], para[password], para[nickname], para[username]+'_head.png')
                    return json.dumps({rescode:SUCCESS})
            except BaseException, e:
                print "Trace back:",e
                return json.dumps({"rescode":SERVER_ERROR})            
    def POST(self):
        para = web.input()
        if not username in para:
            return json.dumps({rescode:PARA_ERROR})
        else:
            try:
                if username not in para or password not in para \
                    or nickname not in para:
                    return json.dumps({rescode:PARA_ERROR})
                elif ifExistUser(para[username]):
                    return json.dumps({rescode:USER_EXIST})
                else:
                    addUser(para[username], para[password], para[nickname], para[username]+'_head.png')
                    return json.dumps({rescode:SUCCESS})
            except BaseException, e:
                print "Trace back:",e
                return json.dumps({"rescode":SERVER_ERROR})            
        
class SignIn:
    def GET(self):
        para = web.input()
        print para
        print para["username"], para["password"]
    def POST(self):
        para = web.input()
        if not username in para:
            return json.dumps({rescode:PARA_ERROR})
        else:
            try:
                if username not in para or password not in para:
                    return json.dumps({rescode:PARA_ERROR})
                elif not ifExistUser(para[username]):
                    return json.dumps({rescode:USER_ERROR})
                else:
                    if verifyPassword(para[username], para[password]):
                        return json.dumps({rescode:SUCCESS})
                    else:
                        return json.dumps({rescode:PASS_ERROR})
            except BaseException, e:
                print "Trace back:",e
                return json.dumps({"rescode":SERVER_ERROR})            

class Pict:
    def GET(self):
        para = web.input()
        print para["username"], para["password"]
    def POST(self):
        para = web.input()
        if not username or not request in para:
            return json.dumps({rescode:PARA_ERROR})
        elif not ifExistUser(para[username]):
            return json.dumps({rescode:USER_ERROR})
        # Upload the head image
        elif para[request] == 'uploadHead' and head in para:
            pict = para[head]
            try:
                filename = pict_dir + para[username] + '_head.png'
                if os.path.isfile(filename):
                    os.remove(filename)
                open(filename, 'wb').write(pict.decode('utf-8').decode('hex'))
                return json.dumps({rescode:SUCCESS})
            except BaseException, e:
                print 'Trace back: ', e
                return json.dumps({rescode:SERVER_ERROR})
        # Download the head image
        elif para[request] == 'downloadHead':
            try:
                filename = pict_dir + para[username] + '_head.png'
                if not os.path.isfile(filename):
                    return json.dumps({rescode:REQ_ERROR})
                else:
                    pict = open(filename, 'rb').read().encode('hex').encode('utf-8')
                    return json.dumps({rescode:SUCCESS, head:pict})
            except BaseException, e:
                print 'Trace back: ', e
                return json.dumps({rescode:SERVER_ERROR})
        # Upload the item image
        elif para[request] == 'uploadItem' and image in para and item_id in para:
            pict = para[image]
            try:
                if not ifItemExist(para[item_id]):
                    return json.dumps({rescode:ITEM_NOT_EXIST})
                filename = head_dir + para[item_id] + '_image.png'
                if os.path.isfile(filename):
                    os.remove(filename)
                open(filename, 'wb').write(pict.decode('utf-8').decode('hex'))
                return json.dumps({rescode:SUCCESS})
            except BaseException, e:
                print 'Trace back: ', e
                return json.dumps({rescode:SERVER_ERROR})
        # Download the item image
        elif para[request] == 'downloadItem' and item_id in para:
            try:
                if not ifItemExist(para[item_id]):
                    return json.dumps({rescode:ITEM_NOT_EXIST})
                filename = head_dir + para[item_id] + '_image.png'
                if not os.path.isfile(filename):
                    return json.dumps({rescode:REQ_ERROR})
                else:
                    pict = open(filename, 'rb').read().encode('hex').encode('utf-8')
                    return json.dumps({rescode:SUCCESS, image:pict})
            except BaseException, e:
                print 'Trace back: ', e
                return json.dumps({rescode:SERVER_ERROR})
        else:
            return json.dumps({rescode:PARA_ERROR})

class Message:
    def GET(self):
        para = web.input()
        print para
    def POST(self):
        para = web.input()
        if not username or not request in para:
            return json.dumps({rescode:PARA_ERROR})
        elif not ifExistUser(para[username]):
            return json.dumps({rescode:USER_ERROR})
        elif para[request] == 'updateMessage':
            try:
                if college not in para or qq not in para or grade not in para or phone not in para:
                    return json.dumps({rescode:PARA_ERROR})
                else:    
                    updateMessage(para[username], para[college], para[qq], para[grade], para[phone])
                    return json.dumps({rescode:SUCCESS})
            except BaseException, e:
                print 'Trace back: ', e
                return json.dumps({rescode:SERVER_ERROR})
        elif para[request] == 'getMessage':
            try:
                para = getMessage(para[username])
                return json.dumps({rescode:SUCCESS, nickname:para[0][1], college:para[0][4], \
                    qq:para[0][5], grade:para[0][6], phone:para[0][7]})
            except BaseException, e:
                print 'Trace back: ', e
                return json.dumps({rescode:SERVER_ERROR})
        elif para[request] == 'updatePassword':
            print para
            try:
                if oldpassword not in para or newpassword not in para:
                    return json.dumps({rescode:PARA_ERROR})
                elif not verifyPassword(para[username], para[oldpassword]):
                    return json.dumps({rescode:PASS_ERROR})
                else:    
                    updatePassword(para[username], para[newpassword])
                    return json.dumps({rescode:SUCCESS})
            except BaseException, e:
                print 'Trace back: ', e
                return json.dumps({rescode:SERVER_ERROR})
        elif para[request] == 'updateNickname':
            try:
                if nickname not in para:
                    return json.dumps({rescode:PARA_ERROR})
                else:    
                    updateNickname(para[username], para[nickname])
                    return json.dumps({rescode:SUCCESS})
            except BaseException, e:
                print 'Trace back: ', e
                return json.dumps({rescode:SERVER_ERROR})
        else:
            return json.dumps({rescode:PARA_ERROR})
                       
class Type:
    def POST(self):
        para = web.input()            
        if not typename in para or not request in para:
            return json.dumps({rescode:PARA_ERROR})
        elif para[request] == 'addType':
            try:
                if ifTypeExist(para[typename]):
                    return json.dumps({rescode:TYPE_EXIST})
                if typetext in para:
                    addType(para[typename], para[typetext])
                else:
                    addType(para[typename])
                return json.dumps({rescode:SUCCESS})
            except BaseException, e:
                print 'Trace back: ', e
                return json.dumps({rescode:SERVER_ERROR})
        elif para[request] == 'getType':
            try:
                if not ifTypeExist(para[typename]):
                    return json.dumps({rescode:TYPE_NOT_EXIST})
                else:
                    text = getType(para[typename])
                    return json.dumps({rescode:SUCCESS, typename:para[typename],\
                        typetext:text})
            except BaseException, e:
                print 'Trace back: ', e
                return json.dumps({rescode:SERVER_ERROR})
        elif para[request] == 'delType':
            try:
                if not ifTypeExist(para[typename]):
                    return json.dumps({rescode:TYPE_NOT_EXIST})
                delType(para[typename])
                return json.dumps({rescode:SUCCESS}) 
            except BaseException, e:
                print 'Trace back: ', e
                return json.dumps({rescode:SERVER_ERROR})
        elif para[request] == 'updateType':
            try:
                if not ifTypeExist(para[typename]):
                    return json.dumps({rescode:TYPE_NOT_EXIST})
                if not typetext in para:
                    return json.jumps({rescode:PARA_ERROR})
                updateType(para[typename], para[typetext])
                return json.dumps({rescode:SUCCESS}) 
            except BaseException, e:
                print 'Trace back: ', e
                return json.dumps({rescode:SERVER_ERROR})
        else:
            return json.dumps({rescode:PARA_ERROR})

class Seller:
    def GET(self):
        pass
    def POST(self):
        para = web.input()
        print para
        if not username in para or not request in para:
            return json.dumps({rescode:PARA_ERROR})
        elif not ifExistUser(para[username]):
             return json.dumps({rescode:USER_ERROR})
        elif para[request] == 'getItemId':
            try:
                if not item_name in para or not item_text in para or \
                    not item_time in para or not item_price in para:
                    return json.dumps({rescode:PARA_ERROR})
                else:
                    new_id = getItemId(para[item_name], para[item_text], para[item_time], para[item_price])
                    if new_id == -1:
                        return json.dumps({rescode:ITEM_NOT_EXIST})
                    else:
                        return json.dumps({rescode:SUCCESS, item_id:new_id})
            except BaseException, e:
                print 'Trace back: ', e
                return json.dumps({rescode:SERVER_ERROR})
        elif para[request] == 'addItem':
            try:
                if not item_name in para or not item_text in para or \
                    not item_time in para or not typename in para or item_price not in para:
                    return json.dumps({rescode:PARA_ERROR})
                else:
                    new_id = str(addItem(para[item_name], para[item_text], para[item_time], para[item_price]))
                    addItemFromUser(new_id, para[username])
                    addItemToType(new_id, para[typename])
                    return json.dumps({rescode:SUCCESS, item_id:new_id})
            except BaseException, e:
                print 'Trace back: ', e
                return json.dumps({rescode:SERVER_ERROR})
        elif para[request] == 'getItem':
            try:
                if not item_id in para:
                    return json.dumps({rescode:PARA_ERROR})
                else:
                    data = {}
                    arr = getItem(str(para[item_id]))
                    if arr == -1:
                        data[rescode] = ITEM_NOT_EXIST
                    else:
                        data[item_name] = arr[1]
                        data[item_text] = arr[2]
                        data[item_time] = arr[3]
                        data[buy_flag] = arr[6]
                        data[item_price] = arr[4]
                        data[username] = getItemFromUser(str(para[item_id]))
                        data[typename] = getItemToType(str(para[item_id]))
                        data[rescode] = SUCCESS
                    return json.dumps(data)
            except BaseException, e:
                print 'Trace back: ', e
                return json.dumps({rescode:SERVER_ERROR})
        elif para[request] == 'delItem':
            try:
                if not item_id in para:
                    return json.dumps({rescode:PARA_ERROR})
                elif not ifItemExist(para[item_id]):
                    return json.dumps({rescode:ITEM_NOT_EXIST})
                else:
                    delItemFromUser(str(para[item_id]))
                    delItemToType(str(para[item_id]))
                    delItemForUser(str(para[item_id]), para[username])
                    delItem(str(para[item_id]))
                    return json.dumps({rescode:SUCCESS})
            except BaseException, e:
                print 'Trace back: ', e
                return json.dumps({rescode:SERVER_ERROR})
        elif para[request] == 'updateItemType':
            try:
                if not item_id in para or not typename in para:
                    return json.dumps({rescode:PARA_ERROR})
                elif not ifItemExist(para[item_id]):
                    return json.dumps({rescode:ITEM_NOT_EXIST})
                else:
                    updateItemToType(str(para[item_id]), para[typename])
                    return json.dumps({rescode:SUCCESS})
            except BaseException, e:
                print 'Trace back: ', e
                return json.dumps({rescode:SERVER_ERROR})
        elif para[request] == 'updateItem':
            try:
                if not item_id in para or not item_name in para or \
                    not item_text in para or not item_time in para or not item_price in para:
                    return json.dumps({rescode:PARA_ERROR})
                elif not ifItemExist(para[item_id]):
                    return json.dumps({rescode:ITEM_NOT_EXIST})
                else:
                    updateItem(str(para[item_id]), para[item_name], para[item_text], para[item_time], para[item_price])
                    return json.dumps({rescode:SUCCESS})
            except BaseException, e:
                print 'Trace back: ', e
                return json.dumps({rescode:SERVER_ERROR})
        elif para[request] == 'getSeller':
            try:
                if not item_id in para:
                    return json.dumps({rescode:PARA_ERROR})
                elif not ifItemExist(para[item_id]):
                    return json.dumps({rescode:ITEM_NOT_EXIST})
                else:
                    seller = getSeller(para[item_id])
                    if seller == -1:
                        return json.dumps({rescode:REQ_ERROR})
                    else:
                        return json.dumps({rescode:SUCCESS, username:seller})
            except BaseException, e:
                print 'Trace back: ', e
                return json.dumps({rescode:SERVER_ERROR})
        elif para[request] == 'resellItem':
            try:
                if not item_id in para:
                    return json.dumps({rescode:PARA_ERROR})
                elif not ifItemExist(para[item_id]):
                    return json.dumps({rescode:ITEM_NOT_EXIST})
                else:
                    seller = getSeller(para[item_id])
                    if seller == -1:
                        return json.dumps({rescode:REQ_ERROR})
                    elif seller != para[username]:
                        return json.dumps({rescode:USER_ERROR})
                    else:
                        resellItem(str(para[item_id]))
                        delItemForUser(para[item_id], para[username])
                        return json.dumps({rescode:SUCCESS})
            except BaseException, e:
                print 'Trace back: ', e
                return json.dumps({rescode:SERVER_ERROR})
        elif para[request] == 'getSellingItems':
            try:
                dic = getSellingItems(para[username])
                dic[rescode] = SUCCESS
                return json.dumps(dic)
            except BaseException, e:
                print 'Trace back: ', e
                return json.dumps({rescode:SERVER_ERROR})
        elif para[request] == 'getOwnItems':
            try:
                dic = getOwnItems(para[username])
                dic[rescode] = SUCCESS
                return json.dumps(dic)
            except BaseException, e:
                print 'Trace back: ', e
                return json.dumps({rescode:SERVER_ERROR})
        elif para[request] == 'getUserItems':
            try:
                if other_user not in para:
                    return json.dumps({rescode:PARA_ERROR})
                else:
                    dic = getUserItems(para[other_user])
                    dic[rescode] = SUCCESS
                    return json.dumps(dic)
            except BaseException, e:
                print 'Trace back: ', e
                return json.dumps({rescode:SERVER_ERROR})
        else:
            return json.dumps({rescode:PARA_ERROR})
   
class Buyer:
    def GET(self):
        pass
    def POST(self):
        para = web.input()
        print para
        if not username in para or not request in para:
            return json.dumps({rescode:PARA_ERROR})
        elif not ifExistUser(para[username]):
             return json.dumps({rescode:USER_ERROR})
        elif para[request] == 'buyItem':
            try:
                if not item_id in para:
                    return json.dumps({rescode:PARA_ERROR})
                elif not ifItemExist(para[item_id]):
                    return json.dumps({rescode:ITEM_NOT_EXIST})
                else:
                    buyItem(str(para[item_id]))
                    addItemForUser(para[item_id], para[username])
                    return json.dumps({rescode:SUCCESS})
            except BaseException, e:
                print 'Trace back: ', e
                return json.dumps({rescode:SERVER_ERROR})
        elif para[request] == 'getBuyer':
            try:
                if not item_id in para:
                    return json.dumps({rescode:PARA_ERROR})
                elif not ifItemExist(para[item_id]):
                    return json.dumps({rescode:ITEM_NOT_EXIST})
                else:
                    buyer = getBuyer(para[item_id])
                    if buyer == -1:
                        return json.dumps({rescode:NOT_BUYED})
                    else:
                        return json.dumps({rescode:SUCCESS, username:buyer})
            except BaseException, e:
                print 'Trace back: ', e
                return json.dumps({rescode:SERVER_ERROR})


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()


