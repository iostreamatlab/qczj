# -*- coding: UTF-8 -*-
"""
 获取汽车之家普拉多的排序
"""
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


def get_review():
    car_list=[]
    response=requests.get("https://www.autohome.com.cn/46/#pvareaid=3311277")
    soup=BeautifulSoup(response.text,"lxml")
    soup=soup.find("ul","rank-list")
    
    for tag_li in soup.find_all('li'):
        dict={}
        dict['rank']=tag_li.find('span','rank-index').string
        dict['name']=tag_li.find('span','rank-name').text
        dict['score']=tag_li.find('span','rank-score').text
        car_list.append(dict)
    return car_list


if __name__ == "__main__":
    
    car_list=get_review()
    print repr(car_list).decode("unicode–escape")

    
       


    