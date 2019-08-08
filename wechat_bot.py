#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itchat, time
from itchat.content import *
from datetime import datetime, timedelta
# 自动回复
# 封装好的装饰器，当接收到的消息是Text，即文字消息
start_time = datetime.now()
@itchat.msg_register(TEXT)
def text_reply(msg):
    # 当消息不是由自己发出的时候
    #return  u"[你好，这是机器人自动回复]{}".format(msg['Text'])
    msg_list = {'1':'请访问以下网址，在空栏处预约时间 https://docs.google.com/spreadsheets/d/1jVAJgKS7CHZaLsPHObHvJBC5JFg9mvIkjTQAtjztAt8/edit?usp=sharing',
                '2':'每天努力多努力三分钟，一个月就多一节课！',
                '3':'',
                '4':''}
    global start_time
    if start_time < datetime.now() :           
        if msg.text in msg_list :
            msg.user.send(msg_list[msg.text])
        elif 'pause' in msg.text :
            pause_minutes = int(msg.text.replace('pause',''))
            start_time = datetime.now() +  timedelta(minutes=pause_minutes)  
        else :
            msg.user.send('[你好我是丘比，现在主人正在休息，请回复]'
                            '1：预约面谈；2：听鸡汤')

        # 回复给好友
if __name__ == '__main__':
    itchat.auto_login(enableCmdQR=2)#enablecmdqr参数是用于在命令行上生成二维码，用于linux服务器
    itchat.run(debug=True)
