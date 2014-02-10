#coding: utf-8
import datetime

today = datetime.datetime.now()
if today.weekday() < 4:
    print('仕事')
elif today.weekday() == 4:
    print('明日は休みだ')
else:
    print('休み')
