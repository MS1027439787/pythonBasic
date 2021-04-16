import json
import sys
import datetime

sys.path.append('../../')
print(sys.path)

# json.dumps函数,字典转换为字符串
a = {'name': 'wang', 'age': 29}
print(a), print(type(a))
b = json.dumps(a)
print(b), print(type(b))

# json.loads函数,将字符串加载为字典
c = json.loads(b)
print(c), print(type(c))

# 时间函数
time = datetime.datetime.now()
# 2021-04-16 11:40:12.850365
print(time)

day = datetime.date.today()
# 2021-04-16
print(day)

# 获取明天/前n天
time = datetime.date.today() + datetime.timedelta(days=1)
print(time)

time = datetime.date.today() - datetime.timedelta(days=2)
print(time)

# 时间类型转换
time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(time)

time = datetime.datetime.now().date()
print(time)
