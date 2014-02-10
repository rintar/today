#coding: utf-8
import datetime

today = datetime.datetime.now()
if today.weekday() < 5:
    print('仕事')
else:
    print('休み')
