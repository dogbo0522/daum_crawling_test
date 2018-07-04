from itertools import count
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as ps
import requests
import re

# reviewList = []


def daum_movie():
    reviewList = []
    for page in count(start=1):
        url = 'http://movie.daum.net/moviedb/grade?movieId=111293&type=netizen&page=%s' % page
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        review_div = soup.find_all('div', 'review_info')
        if page >=94:
            break;

        for n in review_div:
            grade = n.find('em', 'emph_grade').get_text().strip()
            review = n.find('p', 'desc_review').get_text().strip().replace('\r', '')
            date = n.find('span', 'info_append').get_text().strip()[2:10]

            # month = int(date[4])
            # day = int(date[6:])

            # for m in range(12, 1, -1):
            #
            #     for d in range(31, 1, -1):
            #         if m==month and d==day:
            reviewList.append([date,grade,review])
    fileName='/Users/JS-K/Documents/json/daum_review_20185341_00704.txt'
    table = ps.DataFrame(reviewList)
    table.to_csv(fileName, encoding='utf-8-sig', mode='w', index=True)
    print('----------------------saved------------------------')
    return reviewList

result = daum_movie()


