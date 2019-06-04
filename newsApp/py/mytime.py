from datetime import datetime
# timedelta 用于时间加减
from datetime import timedelta


def get_next_hour():
    time = datetime.now()
    formatTime = (time.strftime('%H:%M:%S'))
    # 截取分钟
    minute = formatTime[3:5]
    # 转换为int
    int_minute = int(minute)

    next_hour = time + timedelta(hours=1) - timedelta(minutes=int_minute)
    next_hour = (next_hour.strftime('%Y年%m月%d日 %H:%M'))

    # print(type(formatTime))
    # print(formatTime)
    # print(int_minute)
    # print(next_hour)
    return next_hour


# 返回下一个整十分钟时间
def next_10_minute():
    time = datetime.now()
    formatTime = (time.strftime('%H:%M:%S'))
    # 截取分钟的个位
    minute = formatTime[4:5]
    # 转换为int
    int_minute = int(minute)

    next_10_m = time + timedelta(minutes=10) - timedelta(minutes=int_minute)
    next_10_m = (next_10_m.strftime('%Y年%m月%d日 %H:%M'))

    # print(type(formatTime))
    # print(formatTime)
    # print(int_minute)
    # print(next_10_m)
    return next_10_m


# 返回下一个整5分钟时间
def next_5_minute():
    time = datetime.now()
    formatTime = (time.strftime('%H:%M:%S'))
    # 截取分钟的个位
    minute = formatTime[4:5]
    # 转换为int
    int_minute = int(minute)

    if (int_minute >= 5):
        next_5_m = time + timedelta(minutes=5) - timedelta(minutes=(int_minute - 5))
        next_5_m = (next_5_m.strftime('%Y年%m月%d日 %H:%M'))
    else:
        next_5_m = time + timedelta(minutes=5) - timedelta(minutes=int_minute)
        next_5_m = (next_5_m.strftime('%Y年%m月%d日 %H:%M'))

    # print(type(formatTime))
    # print(formatTime)
    # print(int_minute)
    # print(next_5_m)
    return next_5_m

