import requests
from bs4 import BeautifulSoup
from datetime import datetime

def date_time(number):
    year = datetime.today().year
    month = datetime.today().month
    day = datetime.today().day
    year = str(year)[2:]
    day = day - 1

    if month < 10:
        month = "0" + str(month)
    if day < 10:
        day = "0" + str(day)

    if number == 1:
        return str(year)+'.'+str(month)+'.'+str(day)
    else:
        return str(year)+str(month)+str(day)

def naver_movie_review():
