from newsApp.py import mytime
from datetime import datetime
# timedelta 用于时间加减
from datetime import timedelta

time = datetime.now()
formatTime = (time.strftime('%H:%M:%S'))
# 截取分钟的个位
minute = formatTime[4:5]
# 转换为int
int_minute = int(minute)
if(int_minute >= 5):
    next_5_m = time + timedelta(minutes=5) - timedelta(minutes=(int_minute-5))
    next_5_m = (next_5_m.strftime('%Y年%m月%d日 %H:%M'))
else:
    next_5_m = time + timedelta(minutes=5) - timedelta(minutes=int_minute)
    next_5_m = (next_5_m.strftime('%Y年%m月%d日 %H:%M'))


print(formatTime)
print(int_minute)
print(next_5_m)