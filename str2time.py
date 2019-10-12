# encoding: utf-8
import time
import datetime


# 将str类型的时间转换为datetime
def str2time(timestr):
    time_tuple = time.strptime(timestr, '%Y-%m-%d %H:%M:%S')
    year, month, day, hour, minute, second = time_tuple[:6]
    a_date = datetime.datetime(year, month, day, hour, minute, second)
    return a_date
