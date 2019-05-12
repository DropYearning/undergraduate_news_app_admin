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

