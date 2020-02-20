import requests
from bs4 import BeautifulSoup

# request module을 이용해서 정보 받아옴
url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&amp;theatercode=0013&amp;date=20200223'
html = requests.get(url)
# print(html.text)
soup = BeautifulSoup(html.text, 'html.parser')
# copy selector : movie title
soup.select_one('body > div > div.sect-showtimes > ul > li:nth-child(1) > div > div.info-movie > a > strong')
title_list = soup.select('div.info-movie')
for i in title_list:
    print(i.select_one('a > strong').text.strip()) # text는 태그 제외한 글자만 받아오는 것