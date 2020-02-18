#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itchat, time
from itchat.content import *
from datetime import datetime, timedelta

if __name__ == '__main__':
    itchat.auto_login(enableCmdQR=True)
    itchat.run()

# select friend who you want to send regular messages to
users = itchat.search_friends(name=u'大福団子')
# get UserName
userName = users[0]['UserName']

while 1:
    now = datetime.now()
    now_str = now.strftime('%Y/%m/%d %H:%M:%S')[11:]
    if now_str in ['18:00:05']:
        itchat.send('[Strong]', toUserName = userName)
    time.sleep(1)

