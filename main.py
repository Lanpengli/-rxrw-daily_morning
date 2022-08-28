'''from datetime import date, datetime
import math
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
import os
import random

today = datetime.now()
start_date = os.environ['START_DATE']
city = os.environ['CITY']
birthday = os.environ['BIRTHDAY']

app_id = os.environ["APP_ID"]
app_secret = os.environ["APP_SECRET"]

user_id = os.environ["USER_ID"]
template_id = os.environ["TEMPLATE_ID"]


def get_weather():
  url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city
  res = requests.get(url).json()
  weather = res['data']['list'][0]
  return weather['weather'], math.floor(weather['temp'])

def get_count():
  delta = today - datetime.strptime(start_date, "%Y-%m-%d")
  return delta.days

def get_birthday():
  next = datetime.strptime(str(date.today().year) + "-" + birthday, "%Y-%m-%d")
  if next < datetime.now():
    next = next.replace(year=next.year + 1)
  return (next - today).days

def get_words():
  words = requests.get("https://api.shadiao.pro/chp")
  if words.status_code != 200:
    return get_words()
  return words.json()['data']['text']

def get_random_color():
  return "#%06x" % random.randint(0, 0xFFFFFF)


client = WeChatClient(app_id, app_secret)

wm = WeChatMessage(client)
wea, temperature = get_weather()
data = {"weather":{"value":wea},"temperature":{"value":temperature},"love_days":{"value":get_count()},"birthday_left":{"value":get_birthday()},"words":{"value":get_words(), "color":get_random_color()}}
res = wm.send_template(user_id, template_id, data)
print(res)
user_id = os.environ["USER_ID_1"]
res = wm.send_template(user_id, template_id, data)'''
import math
import random
from datetime import date, datetime

import requests
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage

# import const
import time
# today = datetime.now()
# start_date = os.environ['START_DATE']
# city = os.environ['CITY']
# birthday = os.environ['BIRTHDAY']
#
# app_id = os.environ["APP_ID"]
# app_secret = os.environ["APP_SECRET"]
#
# user_id = os.environ["USER_ID"]
# template_id = os.environ["TEMPLATE_ID"]

today = datetime.now()
start_date = '2022-08-17'

city_1 = '宜昌'
city_2 = '北海'

birthday = '12-21'

APP_ID = 'wx2113507a6a3f32c1'
APP_SECRET = 'a05b06a2edfba6e2e0241357ab0391e1'

user_id_test = 'o41cX6CjmkZRN-yyVwcs6TaaKB3s'
user_id_xx = 'o41cX6AOuxNExpqXtBnHd-8cvRro'

template_id_2 = 'GIWnzoyHICs4QoPizRgG0esrwH87ILeQSD_kIH4nA2g'

# 嗨小小，要开心呀~	今日宜昌天气：{{weather.DATA}} 温度：{{temperature.DATA}} 有点冷哦要及时增添衣物，不要冻感冒啦 今天是我们认识的第{{love_days.DATA}}天 距离小小的生日还有{{birthday_left.DATA}}天 {{words.DATA}} {{secentence.DATA}}

# template_id_3='WAmDKm_GhJAi-WRnZ-_aFs3l03dpkN3PTT2tu4KVugI'
# #筱潇终于到啦~	下飞机后带好行李打个车和朋友快快去学校，要时刻注意安全！！！ 今天是{{date.DATA}} 银海天气：{{weather_2.DATA}} 温度：{{temperature_2.DATA}} 宜昌天气：{{weather_1.DATA}} 温度：{{temperature_1.DATA}} 小小每天关注一下天气状况噢，要照顾好自己呀 今天是我们认识的第{{love_days.DATA}}天 距离筱潇的生日还有{{birthday_left.DATA}}天 {{words.DATA}}
template_id_3='XWUpISYJsH22DD1n6Gy91L7l-TQmJ4NPHa3R-zSH6mQ'

def getweek():
    """
    TODO:
    Wednesday 匹配数据出错，暂时无法解决
    :return:
    """
    try:
        week_en = time.strftime("%A", time.localtime(time.time()))
        week_list = {
            "Monday": "星期一",
            "Tuesday": "星期二",
            "Wednesday ": "星期三",
            "Thursday": "星期四",
            "Friday": "星期五",
            "Saturday": "星期六",
            "Sunday": "星期日"
        }
        currentTime = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        week = week_list[week_en]
        day = currentTime + ' ' + week
        return day
    except Exception as e:
        currentTime = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        day = currentTime + '  星期三'
        return day

print(getweek())



def get_weather(city_id):
    url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city_id
    res = requests.get(url).json()
    weather = res['data']['list'][0]
    return weather['weather'], math.floor(weather['temp'])


def get_count():
    delta = today - datetime.strptime(start_date, "%Y-%m-%d")
    return delta.days


def get_birthday():
    next = datetime.strptime(str(date.today().year) + "-" + birthday, "%Y-%m-%d")
    if next < datetime.now():
        next = next.replace(year=next.year + 1)
    return (next - today).days


def get_words():
    words = requests.get("https://api.shadiao.pro/chp")
    if words.status_code != 200:
        return get_words()
    return words.json()['data']['text']


def get_random_color():
    return "#%06x" % random.randint(0, 0xFFFFFF)


client = WeChatClient(APP_ID, APP_SECRET)

wm = WeChatMessage(client)
wea_1, temperature_1 = get_weather(city_1)
wea_2, temperature_2 = get_weather(city_2)
# wea_3, temperature_3 = get_weather(city_3)
data = {"weather_1": {"value": wea_1, "color": get_random_color()},
        "temperature_1": {"value": temperature_1, "color": get_random_color()},
        "date": {"value": getweek(), "color": get_random_color()},  # 日期
        # "weather_2": {"value": wea_2, "color": get_random_color()},
        # "temperature_2": {"value": temperature_2, "color": get_random_color()},

        "weather_2": {"value": wea_2, "color": get_random_color()},
        "temperature_2": {"value": temperature_2, "color": get_random_color()},

        "love_days": {"value": get_count(), "color": get_random_color()},
        "birthday_left": {"value": get_birthday(), "color": get_random_color()},
        "words": {"value": get_words(), "color": get_random_color()}

        }
#res = wm.send_template(user_id_xx, template_id_3, data)
#print(res)
res = wm.send_template(user_id_test, template_id_3, data)
print(res)
